---
description: Run pre-deploy checks and guide through the deployment process
---

Execute the following deployment checklist before and during deployment:

### Pre-deploy
- [ ] All tests pass
- [ ] No `.env` or secrets staged in git
- [ ] Environment variables are set in the target environment
- [ ] Database migrations are ready to run (if applicable)
- [ ] Build succeeds without errors or warnings

### Deploy steps
1. Run the build and surface any errors
2. Apply database migrations (if applicable)
3. Deploy to the target environment
4. Confirm the deployment succeeded (health check / smoke test)

### Post-deploy
- [ ] Verify the app is responding correctly
- [ ] Check logs for unexpected errors
- [ ] Confirm rollback plan is ready if issues arise

Follow the project rules:
- Code style: @rules/code-style.md
- API conventions: @rules/api-conventions.md

If any pre-deploy check fails, stop and report what needs to be resolved before proceeding.
