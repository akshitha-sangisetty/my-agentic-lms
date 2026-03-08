# Handoff — 2026-03-08 UTC

## Agent Identity
- Task: Full project scaffold from scratch — monorepo, backend, frontend, packages
- Branch: main (no git initialized yet)

## Completed
- Turborepo monorepo structure with `turbo.json`, root `package.json`, `Makefile`
- `docker-compose.yml` for all local infra: Postgres 16, Valkey 8, Weaviate, Neo4j CE, Keycloak 26, MinIO
- `.env.example` with all required environment variables
- `.gitignore` for the full stack

### Backend (apps/api/)
- FastAPI app factory (`main.py`) with CORS, lifespan, health endpoint
- `config.py` with pydantic-settings for all env vars
- `database.py` with async SQLAlchemy engine + session factory
- `dependencies.py` with JWT auth (get_current_user, get_current_faculty, get_current_student)
- **7 SQLAlchemy models**: Institution, User, Course, Assignment, Submission, HintTransaction, Badge
  - All with UUID primary keys, timestamp mixins, proper relationships
  - Enums: UserRole, CourseStatus, GamificationLevel, GradingStrictness, AssignmentType, AssignmentStatus, AppealStatus, HintTier
- **5 Pydantic schema files**: courses, assignments, submissions, gamification, analytics
- **7 route files** with full endpoint stubs matching PRD API spec:
  - courses.py (CRUD + upload + ingestion status + knowledge graph)
  - assignments.py (generate, list, get, update, publish)
  - submissions.py (submit, appeal, AI rationale)
  - gamification.py (profile, leaderboard, hint preview/purchase, streak freeze, badges)
  - tutor.py (WebSocket chat with JWT auth)
  - code_execution.py (sandbox execute)
  - analytics.py (heatmap, summary, at-risk)
- **Service layer stubs** with detailed TODO(agent) markers:
  - ingestion: parser.py, chunker.py, embedder.py
  - assignments: generator.py, publisher.py
  - grading: grader.py, appeal.py, feedback.py
  - gamification: xp_engine.py (IMPLEMENTED), gold_engine.py (IMPLEMENTED), hint_pricing.py (IMPLEMENTED), streaks.py, badges.py, leaderboard.py
  - sandbox: executor.py, test_runner.py
  - analytics: heatmap.py, risk_detector.py
- Event system: event_types.py, publisher.py, consumer.py
- Auth middleware stub
- Alembic config (alembic.ini + env.py) for async migrations

### Shared Packages (packages/)
- **shared**: exceptions.py (AppError hierarchy), pagination.py, event_types.py
- **llm**: provider.py (abstract), vllm_provider.py (OpenAI-compatible), router.py (task-type routing), cost_tracker.py
  - LLM Router routes: creative→72B, grading→72B, tutoring→7B, ingestion→7B, vision→VL-7B
- **rag**: retriever.py, reranker.py, context_builder.py (IMPLEMENTED), grounding.py
- **knowledge-graph**: models.py (ConceptNode, Relationship), client.py, builder.py, queries.py (Cypher templates)
- **agents**: All 5 LangGraph agents scaffolded:
  - IngestionAgent: state, nodes (parse→chunk→embed→build_graph), agent
  - DesignerAgent: state, nodes, prompts (MCQ, scenario, rubric templates), agent
  - TutorAgent: state, nodes, prompts (Socratic, hint tiers), agent
  - GraderAgent: state, nodes, prompts (evaluate, feedback), agent
  - GameEngine: engine.py (IMPLEMENTED — XP/Gold calculation), rules.py (all game rules)

### Frontend (apps/web/)
- Next.js 14 config: package.json, tsconfig, next.config, tailwind.config, postcss
- Custom color palette (brand, gold, xp, streak)
- Root layout + landing page
- Faculty layout + dashboard page stub
- Student layout + dashboard page stub (mission map placeholder)
- API client: base client with auth, courses API, assignments API, gamification API
- TypeScript types mirroring all Pydantic schemas
- Zustand stores: auth, gamification (with optimistic updates)
- Components: UploadZone, XPBar, GoldBalance, StreakCounter, HintButton, TutorChat

## In Progress (Partially Done)
- Service layer: XP, Gold, and Hint Pricing engines are IMPLEMENTED with actual logic. All other services have detailed TODO(agent) stubs.
- Frontend: Core pages are stubs with TODO comments. Components are functional shells.
- Look for `TODO(agent)` markers in these files: All service files, all agent node files, all frontend pages.

## Blocked / Needs Decision
- No git repo initialized yet (user should run `git init`)
- `npm install` not run (user needs to install dependencies)
- No Alembic migration generated yet (need `alembic revision --autogenerate`)
- Need to decide: Keycloak realm setup (OQ — manual or automated?)

## Suggested Next Steps
1. **Initialize git** and make the first commit
2. **Install dependencies**: `cd apps/web && npm install`, `cd apps/api && pip install -e ".[dev]"`
3. **Start infrastructure**: `docker compose up -d`
4. **Generate first Alembic migration**: `cd apps/api && alembic revision --autogenerate -m "initial_schema"`
5. **Implement PDF parser** (services/ingestion/parser.py) — Sprint 1-2 priority
6. **Implement Weaviate embedder** (services/ingestion/embedder.py) — Sprint 2-3 priority
7. **Implement the file upload route** (routes/courses.py upload endpoint → MinIO)
8. **Wire up the IngestionAgent** nodes to actual service calls
9. **Build faculty Course Setup Wizard** (3-step: Upload → Configure → Review)
10. **Build student Mission Map** component

## Files Modified
- Every file listed above was CREATED (project was empty except prd.md and SKILL.md)
- Total: ~80+ files created across the monorepo

## Database Changes
- 7 SQLAlchemy models defined, NO migration generated yet
- Next agent should run: `cd apps/api && alembic revision --autogenerate -m "initial_schema" && alembic upgrade head`

## Environment Changes
- `.env.example` created with all required variables
- Dependencies specified in `apps/api/pyproject.toml` and `apps/web/package.json`
- No packages installed yet — next agent must install
