# DroidCheck • FilePilot • NetPulse

A colorful terminal dashboard for local diagnostics, safe file workflows, and authorized network visibility.

## 15 utilities

**DroidCheck:** system/runtime summary; storage usage; process overview; Python package inventory; diagnostic report export.

**FilePilot:** browse a directory; search filenames; organize files by extension (dry-run first); SHA-256 hashing; find large files.

**NetPulse:** connectivity/latency check; DNS lookup; local interface summary; single-host/single-port TCP reachability; network report export.

Network checks are diagnostic only. Use only on systems and networks you own or are authorized to test. It does not brute-force credentials or scan broad ranges.

## Install

```bash
pip install -r requirements.txt
python main.py
```

Termux:
```bash
pkg update && pkg install python
pip install -r requirements.txt
python main.py
```

Rich provides colorful panels, grouped menus and animated status spinners. Without Rich the core utilities fall back to an ANSI terminal UI. `psutil` provides extra process and interface information when available.

## GitHub integration

In ChatGPT, open Settings → Apps/Connectors → GitHub, authorize the correct GitHub account and grant access to the repository. The connected account in this session is RamizUddin404. Ensure the integration has repository write permission before asking it to commit files.

Never commit tokens, passwords, `.env` files, or private diagnostic reports.
