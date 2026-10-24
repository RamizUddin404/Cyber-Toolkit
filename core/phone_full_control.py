#!/usr/bin/env python3
"""Bounded ADB device diagnostics and explicit file transfer helpers.

This module does not send messages, uninstall applications, bypass device locks,
or attempt to access a device without its normal ADB authorization prompt.
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple


class AdbError(RuntimeError):
    pass


class AdbNotFoundError(AdbError):
    pass


class PhoneFullControl:
    def __init__(self, adb_path: Optional[str] = None, timeout: int = 20):
        if timeout < 1 or timeout > 120:
            raise ValueError("timeout must be between 1 and 120 seconds")
        self.timeout = timeout
        self.adb_path = self._discover_adb(adb_path)

    @staticmethod
    def _discover_adb(provided_path: Optional[str]) -> str:
        candidate = provided_path or "adb"
        found = shutil.which(candidate)
        if not found:
            raise AdbNotFoundError("adb not found in PATH; install Android platform-tools.")
        return found

    def _run(self, args: List[str], timeout: Optional[int] = None) -> subprocess.CompletedProcess:
        if not args or any(not isinstance(arg, str) for arg in args):
            raise ValueError("ADB arguments must be a non-empty list of strings.")
        try:
            return subprocess.run(
                [self.adb_path, *args],
                capture_output=True,
                text=True,
                check=True,
                timeout=timeout or self.timeout,
            )
        except subprocess.CalledProcessError as exc:
            detail = (exc.stderr or exc.stdout or str(exc)).strip()
            raise AdbError(f"ADB command failed: {detail}") from exc
        except subprocess.TimeoutExpired as exc:
            raise AdbError("ADB command timed out.") from exc
        except OSError as exc:
            raise AdbNotFoundError(f"Could not run adb: {exc}") from exc

    def list_connected_devices(self) -> List[Tuple[str, str]]:
        cp = self._run(["devices", "-l"])
        devices = []
        for line in cp.stdout.splitlines():
            if not line.strip() or line.startswith("List of devices"):
                continue
            parts = line.split()
            if len(parts) >= 2:
                devices.append((parts[0], parts[1]))
        return devices

    def device_summary(self, serial: Optional[str] = None) -> dict:
        prefix = ["-s", serial] if serial else []
        cp = self._run([*prefix, "shell", "getprop"])
        return {"serial": serial, "properties": cp.stdout.strip()}

    def connect_device(self, device_address: str) -> str:
        if not device_address or any(c.isspace() for c in device_address):
            raise ValueError("Enter an authorized device address such as 192.168.1.10:5555.")
        return self._run(["connect", device_address]).stdout.strip()

    def disconnect_device(self, device_address: str) -> str:
        if not device_address or any(c.isspace() for c in device_address):
            raise ValueError("Enter the device address to disconnect.")
        return self._run(["disconnect", device_address]).stdout.strip()

    def install_app(self, apk_path: str, reinstall: bool = False) -> str:
        apk = Path(apk_path).expanduser().resolve(strict=True)
        if not apk.is_file() or apk.suffix.lower() != ".apk":
            raise ValueError("Select an existing .apk file.")
        args = ["install"]
        if reinstall:
            args.append("-r")
        args.append(str(apk))
        return self._run(args, timeout=60).stdout.strip()

    def take_screenshot(self, remote_tmp: str = "/sdcard/screen.png",
                        local_out: Optional[str] = None) -> str:
        if not remote_tmp.startswith("/sdcard/") or ".." in Path(remote_tmp).parts:
            raise ValueError("Screenshot path must be under /sdcard/.")
        self._run(["shell", "screencap", "-p", remote_tmp])
        if local_out:
            destination = Path(local_out).expanduser().resolve()
            destination.parent.mkdir(parents=True, exist_ok=True)
            self._run(["pull", remote_tmp, str(destination)])
            return str(destination)
        return remote_tmp

    def record_screen(self, remote_out: str = "/sdcard/demo.mp4", duration_sec: int = 15) -> str:
        if not remote_out.startswith("/sdcard/") or ".." in Path(remote_out).parts:
            raise ValueError("Recording path must be under /sdcard/.")
        duration = max(1, min(int(duration_sec), 60))
        self._run(["shell", "screenrecord", "--time-limit", str(duration), remote_out],
                  timeout=duration + 10)
        return remote_out

    def list_files(self, remote_path: str = "/sdcard/") -> List[str]:
        if not remote_path.startswith("/sdcard/") or ".." in Path(remote_path).parts:
            raise ValueError("File listing is limited to /sdcard/.")
        cp = self._run(["shell", "ls", "-1", remote_path])
        return [line for line in cp.stdout.splitlines() if line]

    def pull_file(self, remote_path: str, local_path: str) -> str:
        if not remote_path.startswith("/sdcard/") or ".." in Path(remote_path).parts:
            raise ValueError("Pull source is limited to /sdcard/.")
        destination = Path(local_path).expanduser().resolve()
        destination.parent.mkdir(parents=True, exist_ok=True)
        self._run(["pull", remote_path, str(destination)], timeout=60)
        return str(destination)

    def push_file(self, local_path: str, remote_path: str) -> str:
        source = Path(local_path).expanduser().resolve(strict=True)
        if not source.is_file():
            raise ValueError("Select an existing regular file.")
        if not remote_path.startswith("/sdcard/") or ".." in Path(remote_path).parts:
            raise ValueError("Push destination is limited to /sdcard/.")
        return self._run(["push", str(source), remote_path], timeout=60).stdout.strip()


def main() -> int:
    try:
        controller = PhoneFullControl()
        print("ADB device diagnostics (authorized devices only)")
        devices = controller.list_connected_devices()
        if not devices:
            print("No authorized ADB devices found. Enable USB debugging and accept the device prompt.")
            return 0
        for index, (serial, state) in enumerate(devices, 1):
            print(f"{index}. {serial} — {state}")
        choice = input("Select a device number for basic device info, or Enter to exit: ").strip()
        if not choice:
            return 0
        if not choice.isdigit() or not (1 <= int(choice) <= len(devices)):
            print("Invalid selection.")
            return 2
        serial, state = devices[int(choice) - 1]
        if state != "device":
            print(f"Device state is {state!r}; authorize it before querying details.")
            return 1
        print(controller.device_summary(serial))
        return 0
    except (AdbError, ValueError, OSError) as exc:
        print(f"[!] {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
