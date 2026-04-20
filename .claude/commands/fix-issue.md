---
description: Investigate and fix a reported issue or bug in the project
---

Fix the issue described by the user using the following process:

1. **Understand** — restate the problem to confirm scope before touching any code
2. **Locate** — find the relevant files, functions, and lines involved
3. **Root cause** — identify *why* the bug occurs, not just *where*
4. **Fix** — apply the minimal change that resolves the root cause without side effects
5. **Verify** — check that existing tests still pass and add a test that covers the fixed case if one is missing

Follow the project rules:
- Code style: @rules/code-style.md
- Testing: @rules/testing.md
- API conventions: @rules/api-conventions.md

Do not refactor surrounding code, add unrelated improvements, or change behaviour outside the scope of the issue.
