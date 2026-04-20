---
description: Code style and formatting rules for this project
---

# Code Style

## General
- Prefer clarity over cleverness — code is read more than it is written
- Keep functions small and focused on a single responsibility
- Avoid deep nesting; return early or extract helpers instead
- No commented-out code — delete it or track it in version control

## Naming
- Use descriptive names; avoid abbreviations unless universally understood (`id`, `url`, `api`)
- Boolean variables and functions should read as assertions: `isLoading`, `hasError`, `canSubmit`
- Functions should be named after what they do, not how they do it

## Formatting
- Follow the formatter config in the repo (Prettier / ESLint / Black / etc.)
- Trailing commas where supported
- Single quotes for strings unless the language convention differs

## Imports
- Group imports: external packages → internal modules → relative paths
- No unused imports

## Comments
- Only comment non-obvious logic — do not restate what the code does
- Use `// TODO:` for known gaps, `// FIXME:` for known bugs
