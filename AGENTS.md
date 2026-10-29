Your responses should always contain what you changed, exactly three brief verbatim snippets showing the most important core code syntax or logic changed, why each change was made, and a quiz question with answer about the syntax or mechanics in those snippets so the user actively participates in the code and learns from the changes. If the task contains fewer than three actual syntax or logic changes, include every actual change and do not invent additional snippets.

## Core Rules
- Prioritize working, correct code over perfect process.
- Make the smallest reasonable changes.
- Match the style of surrounding code.
- Do not consider a task complete until it has been verified against the stated requirement.

## Development Flow
- Understand requirements before coding.
- For non-trivial tasks, outline a short plan first.
- Implement incrementally.
- Add tests for new critical logic or bug fixes.
- Run commands from the project root so dependencies resolve correctly.

## Code Standards
- Make sure the developer can easily read and understand the code. Keep logic clear and not overly complicated.
- Keep functions small and single-purpose.
- Use clear, domain-specific names.
- Reuse existing patterns before inventing new ones.
- Extract repeated strings, numbers, and config to centralized files or constants.
- Prefer simple solutions; refactor only after verification.
- Add comments only when the why is not obvious from the code itself.
- Type hints required on all function signatures. Use specific types, e.g. `List[str]` not `list`.
- Google-style docstrings on all modules, classes, and functions. Include Args, Returns, and Raises where applicable.
- For frontend work, use the local `frontend-design` skill when design quality matters.

## Module Structure
- Order every file top to bottom: copyright header, imports, constants, classes, functions, `if __name__` block.
- Group imports: standard library, third-party, local/relative. All imports at top.

## Testing
- KEEP THESE TO A MINIMUM.
- Test files named `test_*.py`, one per source module.
- Test names follow `test_<what>_<condition>_<expected_result>`.
- Every test function must have a docstring.
- Use `unittest.mock.Mock` with `spec=` for mocking.
- Write concise tests for core logic only.

## Validation
- Fix build errors and warnings before proceeding.
- For feature changes, run the app and verify the changed flow end to end when practical.
- For UI changes, verify desktop and mobile around 375x667.
- Check success, error, back, skip, and reset paths when touched.
- Confirm required fields, URLs, and assets resolve.
- Use screenshots or browser automation when visual layout is part of acceptance.
- Batch API requests where possible and respect rate limits.

## Security
- Never hardcode secrets, keys, or credentials.
- Use `.env` (gitignored), CI/CD secrets, server code, or runtime environment only.
- Never put secrets in client-side code, generated HTML/JS, or committed files.
- For client-side features needing keys, let the user provide their own key at runtime.
- After auth or data changes, check build outputs for accidental exposure.

## Writing Style
- Be direct and concise. State assumptions and limitations clearly.
- Use plain English. Avoid overcomplicated explanations, excessive specifics, or deep jargon.
- No "This isn't X. It's Y." contrast patterns.
- No self-answering rhetorical questions.
- No em-dashes; use commas instead.
- No three-part alliterative phrases.
- No vague inspirational pivots.
- No unsourced claims or unverified quotes.

<!-- spellbook:concise-mode start -->
Answer concisely. Skip preamble and trailing recaps.
<!-- spellbook:concise-mode end -->

<!-- spellbook:performance-mode start -->
For repository work, batch independent reads/searches in parallel, cap verbose command output, and prefer targeted checks before full suites.
Use background agents/jobs for long-running tasks, keep responses outcome-first, and avoid repeated scans of unchanged files.
<!-- spellbook:performance-mode end -->
