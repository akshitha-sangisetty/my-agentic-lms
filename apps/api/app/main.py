from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import courses, assignments, submissions, gamification, tutor, code_execution, analytics


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    # Startup
    yield
    # Shutdown


def create_app() -> FastAPI:
    app = FastAPI(
        title="Agentic LMS API",
        description="AI-powered Learning Management System",
        version="0.1.0",
        lifespan=lifespan,
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins.split(","),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routes
    app.include_router(courses.router, prefix="/api/v1", tags=["courses"])
    app.include_router(assignments.router, prefix="/api/v1", tags=["assignments"])
    app.include_router(submissions.router, prefix="/api/v1", tags=["submissions"])
    app.include_router(gamification.router, prefix="/api/v1", tags=["gamification"])
    app.include_router(tutor.router, prefix="/api/v1", tags=["tutor"])
    app.include_router(code_execution.router, prefix="/api/v1", tags=["code-execution"])
    app.include_router(analytics.router, prefix="/api/v1", tags=["analytics"])

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
