# Claude Team Instructions

This file contains shared instructions for Claude when working on this project.
All team members should keep this file up to date with project-wide conventions.

## Project Overview

**Agentic Compliance & Document Orchestrator** — a boilerplate for building AI-powered compliance workflows and document orchestration systems.

- **Framework**: Next.js (App Router) with TypeScript
- **Database**: PostgreSQL
- **Purpose**: Provides the foundational structure for agentic workflows that handle compliance checking, document processing, and orchestration pipelines.

## Development Guidelines

- Use TypeScript strictly — no `any` types without justification
- Follow the App Router conventions (`app/`, `page.tsx`, `layout.tsx`, `route.ts`)
- API routes live under `app/api/` and follow the REST conventions in `.claude/rules/api-conventions.md`
- Database access goes through a dedicated data layer — never query PostgreSQL directly from components or API routes without an abstraction
- Environment variables for DB connection must be defined in `.env.local` (never committed)

## Common Commands

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Run type checking
npx tsc --noEmit

# Run tests
npm test

# Database migrations
npm run db:migrate
```
