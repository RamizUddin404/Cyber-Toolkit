# Initial Repository Audit

Date: 2026-10-25  
Branch inspected: `main`

## Inventory

- 173 repository paths were returned by the GitHub tree API.
- 147 paths are under `core/`.
- The repository contains the separate `DroidCheck_FilePilot_NetPulse/` Python suite.

## Findings requiring review

1. Several files under `core/` are obfuscated using compressed/base64-encoded
   `marshal` payloads executed dynamically. Static inspection cannot verify their behavior.
2. Tool names include SMS bombing/spoofing, TCP flooding, reverse shells, SQL injection,
   payload generation, password cracking, and web-shell functionality. These should not be
   treated as safe or production-ready without manual review and a tightly controlled lab.
3. Repository paths include `core/pass.txt`, `core/master_pass.txt`,
   `core/target_pass.txt`, and `core/victim_logs.txt`. Their contents and provenance
   should be reviewed privately. If they contain real credentials or personal data, remove
   them from the repository and rotate any exposed credentials; deleting a file in a new
   commit does not remove it from Git history.
4. The existing README claims all tools are fully fixed and working, but a README claim is
   not test evidence. Avoid claiming 100% working until each tool has isolated tests.
5. The legacy installer uses `eval` to run package-manager command strings and may install
   dependencies globally. Prefer explicit command arrays and an isolated Python environment
   where supported.
6. The root launcher invokes `python3` directly rather than the interpreter running the
   current launcher. This can select the wrong interpreter in virtual environments.

## Changes in this audit pass

- Added a GitHub Actions workflow to compile Python sources and run safe unit tests.
- Added a security policy and documented the initial findings.
- Added a static audit helper that reports suspicious patterns without executing files.
- Updated the root launcher to use the active Python interpreter and a checked subprocess.
- This pass does **not** claim that every legacy tool has been functionally tested.
- Obfuscated or potentially harmful tools are not executed by CI.

## Next review sequence

1. Privately inspect or remove any credentials and personal data after confirming their
   contents and provenance.
2. Replace obfuscated code with readable, reviewed implementations where legitimate.
3. Give each supported tool explicit inputs, bounded timeouts, clear errors, and unit tests.
4. Keep destructive, exploitative, credential-attack, and denial-of-service functions out
   of the default menu.
5. Run each approved utility in an isolated Termux/Linux test environment and document
   platform limitations.
