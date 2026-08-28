import shutil
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class AdbError(RuntimeError):
    pass

class AdbNotFoundError(AdbError):
    pass

class PhoneFullControl:
    def __init__(self, adb_path: Optional[str] = None, timeout: Optional[int] = 30):
        self.timeout = timeout
        self.adb_path = self._discover_adb(adb_path)

    def _discover_adb(self, provided_path: Optional[str]) -> str:
        if provided_path:
            if shutil.which(provided_path):
                return provided_path
            raise AdbNotFoundError(f"Provided adb not found at: {provided_path}")
        which = shutil.which("adb")
        if which:
            return which
        raise AdbNotFoundError("adb executable not found in PATH. Install ADB or provide path.")

    def _run(self, args: List[str], capture_output: bool = True, check: bool = True, timeout: Optional[int] = None) -> subprocess.CompletedProcess:
        cmd = [self.adb_path] + args
        timeout = timeout if timeout is not None else self.timeout
        try:
            logger.debug("Running command: %s", cmd)
            cp = subprocess.run(cmd, capture_output=capture_output, text=True, check=check, timeout=timeout)
            return cp
        except subprocess.CalledProcessError as e:
            logger.error("ADB command failed (%s): %s", e.returncode, e.stderr)
            raise AdbError(f"ADB command failed: {e}") from e
        except subprocess.TimeoutExpired as e:
            logger.error("ADB command timed out: %s", cmd)
            raise AdbError(f"ADB command timed out: {e}") from e
        except FileNotFoundError as e:
            logger.error("ADB not found when attempting to run: %s", cmd)
            raise AdbNotFoundError("ADB not found") from e

    def list_connected_devices(self) -> List[Tuple[str, str]]:
        cp = self._run(["devices", "-l"])
        lines = cp.stdout.strip().splitlines()
        devices = []
        for line in lines:
            if not line or line.startswith("List of devices"):
                continue
            parts = line.split()
            serial = parts[0]
            status = parts[1] if len(parts) > 1 else ""
            devices.append((serial, status))
        return devices

    def connect_device(self, device_ip: str) -> str:
        cp = self._run(["connect", device_ip])
        return cp.stdout.strip()

    def disconnect_device(self, device_ip: str) -> str:
        cp = self._run(["disconnect", device_ip])
        return cp.stdout.strip()

    def install_app(self, apk_path: str, reinstall: bool = False, timeout: Optional[int] = None) -> str:
        p = Path(apk_path)
        if not p.is_file():
            raise FileNotFoundError(f"APK not found: {apk_path}")
        args = ["install"]
        if reinstall:
            args.append("-r")
        args.append(str(p))
        cp = self._run(args, timeout=timeout)
        return cp.stdout.strip()

    def uninstall_app(self, package_name: str) -> str:
        cp = self._run(["uninstall", package_name])
        return cp.stdout.strip()

    def take_screenshot(self, remote_tmp: str = "/sdcard/screen.png", local_out: Optional[str] = None) -> str:
        # Capture on device then pull. Avoid shell redirection.
        self._run(["shell", "screencap", "-p", remote_tmp])
        if local_out:
            local_path = Path(local_out)
            self._run(["pull", remote_tmp, str(local_path)])
            return str(local_path)
        return remote_tmp

    def record_screen(self, remote_out: str = "/sdcard/demo.mp4", duration_sec: int = 30):
        # Use screenrecord on device with --time-limit param
        args = ["shell", "screenrecord", "--time-limit", str(duration_sec), remote_out]
        self._run(args, timeout=duration_sec + 10)

    def send_sms(self, number: str, message: str) -> str:
        # Use argument list and let adb handle quoting; use am start with --es
        args = ["shell", "am", "start", "-a", "android.intent.action.SENDTO", "-d", f"sms:{number}",
                "--es", "sms_body", message, "--ez", "exit_on_sent", "true"]
        cp = self._run(args)
        return cp.stdout.strip()

    def list_files(self, remote_path: str) -> List[str]:
        cp = self._run(["shell", "ls", "-1", remote_path])
        return [line for line in cp.stdout.splitlines() if line]

    def pull_file(self, remote_path: str, local_path: str) -> str:
        local = Path(local_path)
        self._run(["pull", remote_path, str(local)])
        return str(local)

    def push_file(self, local_path: str, remote_path: str) -> str:
        local = Path(local_path)
        if not local.exists():
            raise FileNotFoundError(f"Local file not found: {local_path}")
        cp = self._run(["push", str(local), remote_path])
        return cp.stdout.strip()

if __name__ == "__main__":
    controller = PhoneFullControl()
    print(controller.list_connected_devices())    def take_screenshot(self, output_path):
        os.system(f'{self.adb_path} exec-out screencap -p > {output_path}')

    def record_screen(self, output_path, duration):
        os.system(f'{self.adb_path} screenrecord {output_path} --time-limit {duration}')

    def send_sms(self, number, message):
        os.system(f'{self.adb_path} shell am start -a android.intent.action.SENDTO -d sms:{number} --es sms_body "{message}" --ez exit_on_sent true')

    def list_files(self, remote_path):
        return subprocess.check_output([self.adb_path, 'shell', 'ls', remote_path]).decode().strip()

    def pull_file(self, remote_path, local_path):
        os.system(f'{self.adb_path} pull {remote_path} {local_path}')

    def push_file(self, local_path, remote_path):
        os.system(f'{self.adb_path} push {local_path} {remote_path}')\n\nif __name__ == '__main__':
    phone_control = PhoneFullControl()
    phone_control.connect_device('192.168.1.1')  # Replace with the actual device IP
    # Add further functionality as required
