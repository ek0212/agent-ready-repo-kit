# Exemplary Claude

Source: public gist `cc61c27ceb9affece85112a36eebe526`, "Generic and best CLAUDE.md/AGENTS.md file for coding (especially web apps) after years of testing".

## Core Rules

- Prioritize working, correct code over perfect process.
- Make the smallest reasonable changes.
- Match the style of surrounding code.

## Development Flow

- Understand requirements before coding.
- For non-trivial tasks, outline a short plan first.
- Implement incrementally.
- Add tests for new critical logic or bug fixes.

## Code Standards

- Keep functions small and single-purpose.
- Use clear, domain-specific names.
- Extract repeated strings, numbers, and config to centralized files when they are reused.
- Prefer simple solutions; refactor only after verification.
- No unnecessary comments.
- Type hints required on all function signatures when the language supports them.
- UI on desktop and basic mobile sizes should be coherent.

## Module Structure

- Order files top to bottom: copyright header if present, imports, constants, classes, functions, executable entrypoint.
- Group imports: standard library, third-party, local or relative.
- Keep imports at the top of the file unless the project has a deliberate lazy-loading pattern.

## Testing

- Test files named `test_*.py` for Python projects unless the repo already uses another convention.
- Test names should describe behavior, condition, and expected result.
- Use mocks with specs when possible.

## Feature Flags And Debug

- Use feature flags for experimental, debug, or incomplete work.
- Wrap debug code, logs, or new behavior behind flags.
- Disable or remove debug code in production builds.
- Document flags in a central config or README.
- Never ship code that relies on debug flags being on.

## Security

- Never hardcode secrets or keys.
- Use `.env` files that are gitignored, or runtime/server environment variables.
- After auth or data changes, check build outputs for accidental exposure.

## Writing Style

- Be direct and concise.
- State assumptions and limitations clearly.
- Use plain English.
- Avoid unsourced claims or unverified quotes.

## End-To-End Validation

- Build must succeed with zero errors.
- Test changed functionality manually when behavior changed.
- Check UI on desktop and basic mobile sizes when UI changed.

