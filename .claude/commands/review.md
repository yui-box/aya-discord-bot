---
description: Review code changes for quality, security, and consistency with project standards
---

Review the current changes or the specified files for the following:

1. **Correctness** — logic errors, edge cases, off-by-one errors
2. **Security** — injection risks, exposed secrets, insecure defaults (OWASP Top 10)
3. **Code style** — consistency with @rules/code-style.md
4. **Testing** — adequate coverage per @rules/testing.md
5. **API conventions** — adherence to @rules/api-conventions.md

For each issue found, provide:
- Location (file:line)
- Severity: `critical` | `major` | `minor` | `suggestion`
- Description of the problem
- Recommended fix

End with a summary: overall assessment and whether the code is ready to merge.
