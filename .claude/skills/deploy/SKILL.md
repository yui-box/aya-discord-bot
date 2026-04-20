---
description: Auto-invoked deploy workflow. Triggers when deployment-related files or scripts are modified, or when the user initiates a deploy action.
triggers:
  - deploy
  - release
  - Dockerfile
  - docker-compose
  - .github/workflows
  - ci
  - cd
  - Makefile
---

# Skill: Deploy

This skill runs automatically when deployment configuration or scripts change, or when a deploy is initiated.

## Pre-deploy validation

Before any deployment proceeds, verify:

1. **Tests** — full test suite passes with no failures
2. **Build** — production build completes without errors
3. **Secrets** — no sensitive values are hardcoded; all required env vars are documented
4. **Migrations** — any pending database migrations are safe to run and have a rollback path
5. **Dependencies** — lock file is committed and in sync with the manifest

## Environment promotion flow

```
local → staging → production
```

- Never deploy directly to production without a staging validation step
- Staging must mirror production configuration as closely as possible

## Deploy steps

1. Pull latest from the target branch
2. Run build
3. Run migrations (if applicable)
4. Deploy to target environment
5. Run smoke tests / health check
6. Confirm rollback procedure is ready

## Rollback plan

- Every deploy must have a defined rollback step
- Database migrations must be reversible or the rollback plan must account for schema state
- Keep the previous build artifact available for at least one deploy cycle

## Post-deploy checks

- [ ] Health endpoint returns 200
- [ ] No spike in error rate in logs
- [ ] Key user flows work end-to-end
- [ ] Notify the team of the successful deployment

## On failure

1. Stop the deployment immediately
2. Roll back to the last known good state
3. Document what failed and why before retrying
