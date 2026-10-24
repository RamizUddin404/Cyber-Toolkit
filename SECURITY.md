# Security Policy

## Scope

Cyber-Toolkit is intended for lawful learning, defensive diagnostics, and testing of
systems for which the operator has explicit authorization. Use a local lab, CTF, or
written-approved assessment scope.

## Report a vulnerability

Do not publish exploit details, credentials, private logs, tokens, or personal data in
public issues. Contact the repository maintainer privately through GitHub's security
reporting feature when it is enabled for this repository.

## Repository hygiene

- Never commit passwords, session cookies, access tokens, private logs, or personal data.
- Keep secrets in environment variables or GitHub Actions secrets.
- Review third-party code before running it, especially obfuscated scripts or scripts
  that use `exec`, `eval`, `marshal`, shell pipelines, or network callbacks.
- Run tools without root unless root is genuinely required and the test environment is
  disposable.
- Network checks must stay within explicitly authorized scope.
- Do not use denial-of-service, credential attacks, phishing, persistence, or unauthorized
  access features against real users or systems.

## Testing

The CI workflow syntax-compiles Python files but does not execute the toolkit's scripts.
This is deliberate: a syntax check cannot establish that a tool is safe or functionally
correct. Each tool needs a reviewed implementation and isolated tests before it can be
marked supported.
