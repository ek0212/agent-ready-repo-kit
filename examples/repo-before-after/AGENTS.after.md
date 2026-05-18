# Example Project Agent Instructions

## Project Shape

This repo is a browser extension that processes user-selected page data locally and exports structured results.

## Stable Constraints

- Keep processing local unless the user explicitly enables sync.
- Keep extension permissions minimal.
- Preserve Manifest V3 compatibility.
- Do not add remote scripts.

## Commands

```bash
npm install
npm run lint
npm run build
```

## Conventions

- Reuse existing message-passing helpers.
- Keep content-script DOM access scoped to user-triggered actions.
- Store reusable labels and config in constants.

## Mistakes To Avoid

- Do not request `<all_urls>` unless a feature truly requires it.
- Do not log user-selected page text.
- Do not duplicate export logic.
- Do not put sync credentials in extension storage without an explicit design review.

## Ask Before

- adding permissions
- changing storage behavior
- sending page data to a remote service
- changing the public export format

