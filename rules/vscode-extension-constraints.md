---
paths:
  - "package.json"
  - "**/*.ts"
  - ".vscode/**"
---
# VS Code Extension Constraints

- Follow VS Code extension activation best practices.
- Keep activation events as narrow as possible.
- Avoid blocking the extension host with long synchronous work.
- Store user data only in approved VS Code storage APIs or documented sync locations.
- Webviews must sanitize or control rendered content.
- Do not assume workspace trust.
- Do not rewrite user files without an explicit command or confirmation.
