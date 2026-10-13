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
- Make sure the developer can easily read and understand the code. This means making logic clear and not overly complicated.
- Keep functions small and single-purpose.
- Use clear, domain-specific names.
- Extract repeated strings, numbers, and config to centralized files (should be in constants).
- Prefer simple solutions; refactor only after verification.
- No unnecessary comments.
- Type hints required on all function signatures (arguments and return values). Use specific types (e.g., `List[str]` not `list`).
- Google-style docstrings on all modules, classes, and functions. Include Args, Returns, and Raises where applicable.

## Module Structure
- Order every file top to bottom: copyright header, imports, constants, classes, functions, `if __name__` block.
- Group imports: standard library, then third-party, then local/relative. All at the top of the file.

## Testing
- KEEP THESE TO A MINIMUM.
- Test files named `test_*.py`, one per source module.
- Test names follow `test_<what>_<condition>_<expected_result>`.
- Every test function must have a docstring.
- Use `unittest.mock.Mock` with `spec=` for mocking.

## Security
- Never hardcode secrets or keys.
- Use `.env` (gitignored) or server/runtime environment only.
- After auth or data changes, check build outputs for accidental exposure.

## Writing Style
- Be direct and concise. State assumptions and limitations clearly.
- Use plain English (avoid overcomplicated explanations, excessive specifics, or deep jargon).
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
