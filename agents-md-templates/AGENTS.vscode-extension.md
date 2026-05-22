# VS Code Extension Agent Instructions

Append this to `AGENTS.base.md` for VS Code extensions.

## Stable Constraints

- Follow VS Code extension activation best practices.
- Keep activation events as narrow as possible.
- Store user data only in approved VS Code storage APIs or documented sync locations.
- Avoid blocking the extension host with long synchronous work.

## Commands

```bash
npm install
npm run compile
npm run lint
npm test
```

Adjust commands to match the repo.

## Review Checklist

- `package.json` contributes only commands, views, menus, and activation events that are needed.
- Webviews sanitize or control rendered content.
- File-system access is scoped and intentional.
- Settings are documented and have safe defaults.

## Mistakes To Avoid

- Do not activate on startup unless necessary.
- Do not store tokens in plain project files.
- Do not assume workspace trust.
- Do not rewrite user files without an explicit command or confirmation.
