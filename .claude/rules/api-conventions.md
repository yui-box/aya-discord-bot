---
description: API design and communication conventions for this project
---

# API Conventions

## REST
- Use nouns for resource paths, not verbs: `/users` not `/getUsers`
- Plural resource names: `/users`, `/orders`
- Nest resources to express ownership: `/users/:id/orders`
- HTTP methods map to intent: `GET` read, `POST` create, `PUT`/`PATCH` update, `DELETE` remove

## Request & Response
- Always return JSON with a consistent envelope:
  ```json
  { "data": {}, "error": null }
  ```
- Use `camelCase` for JSON keys
- Dates must be ISO 8601: `2024-01-15T10:30:00Z`
- Never return raw database rows — map to a defined response shape

## Status codes
| Scenario | Code |
|---|---|
| Success | 200 / 201 |
| No content | 204 |
| Bad request / validation | 400 |
| Unauthenticated | 401 |
| Forbidden | 403 |
| Not found | 404 |
| Server error | 500 |

## Error responses
```json
{
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": []
  }
}
```

## Versioning
- Version via URL prefix: `/v1/`, `/v2/`
- Do not make breaking changes within a version

## Security
- Validate and sanitize all input at the boundary
- Never expose internal IDs, stack traces, or system paths in responses
- Require authentication on all endpoints unless explicitly public
