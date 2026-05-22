# Coding Constraints

- Prioritize working, correct code over perfect process.
- Make the smallest reasonable change that satisfies the request.
- Match surrounding code style, naming, structure, and error handling.
- Keep functions small and single-purpose.
- Use clear domain-specific names.
- Declare named constants for meaningful strings, numbers, labels, and config values. No magic literals in business logic.
- Centralize shared constants in an existing constants or config file rather than redefining them per module.
- Refactor only after behavior is verified.
- Add or update tests for new critical logic and bug fixes.
- Use feature flags for experimental, debug, incomplete, or risky rollout behavior.
- Verify with the narrowest relevant command before reporting completion.
