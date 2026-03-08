from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import CurrentUser, get_current_faculty
from app.models.course import Course
from app.schemas.courses import (
    CourseCreateRequest,
    CourseResponse,
    CourseUpdateRequest,
    IngestionStatusResponse,
)

router = APIRouter()


@router.post("/courses", response_model=CourseResponse)
async def create_course(
    body: CourseCreateRequest,
    faculty: CurrentUser = Depends(get_current_faculty),
    db: AsyncSession = Depends(get_db),
) -> Course:
    course = Course(
        institution_id=faculty.institution_id,
        faculty_id=faculty.id,
        **body.model_dump(),
    )
    db.add(course)
    await db.flush()
    return course


@router.get("/courses", response_model=list[CourseResponse])
async def list_courses(
    faculty: CurrentUser = Depends(get_current_faculty),
    db: AsyncSession = Depends(get_db),
) -> list[Course]:
    result = await db.execute(
        select(Course).where(Course.faculty_id == faculty.id).order_by(Course.created_at.desc())
    )
    return list(result.scalars().all())


@router.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course(
    course_id: UUID,
    faculty: CurrentUser = Depends(get_current_faculty),
    db: AsyncSession = Depends(get_db),
) -> Course:
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one()
    return course


@router.patch("/courses/{course_id}", response_model=CourseResponse)
async def update_course(
    course_id: UUID,
    body: CourseUpdateRequest,
    faculty: CurrentUser = Depends(get_current_faculty),
    db: AsyncSession = Depends(get_db),
) -> Course:
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one()
    for field, value in body.model_dump(exclude_unset=True).items():
        setattr(course, field, value)
    await db.flush()
    return course


@router.post("/courses/{course_id}/upload")
async def upload_materials(
    course_id: UUID,
    file: UploadFile,
    faculty: CurrentUser = Depends(get_current_faculty),
    db: AsyncSession = Depends(get_db),
) -> dict:
    # TODO(agent): Implement file upload to MinIO + trigger Ingestion Agent.
    #   1. Upload file to MinIO bucket under courses/{course_id}/
    #   2. Create an ingestion job record
    #   3. Emit ingestion.started event to trigger IngestionAgent
    #   See services/ingestion/parser.py for the parsing pipeline
    return {"status": "accepted", "filename": file.filename, "course_id": str(course_id)}


@router.get("/courses/{course_id}/ingestion-status", response_model=IngestionStatusResponse)
async def get_ingestion_status(
    course_id: UUID,
    faculty: CurrentUser = Depends(get_current_faculty),
) -> IngestionStatusResponse:
    # TODO(agent): Implement ingestion status polling from Valkey.
    return IngestionStatusResponse(
        course_id=course_id,
        status="pending",
        progress_pct=0,
        current_step="not_started",
    )


@router.get("/courses/{course_id}/knowledge-graph")
async def get_knowledge_graph(
    course_id: UUID,
    faculty: CurrentUser = Depends(get_current_faculty),
) -> dict:
    # TODO(agent): Query Neo4j for the course's Knowledge Graph nodes + edges.
    return {"course_id": str(course_id), "nodes": [], "edges": []}


@router.patch("/courses/{course_id}/knowledge-graph/nodes/{node_id}")
async def update_knowledge_graph_node(
    course_id: UUID,
    node_id: str,
    body: dict,
    faculty: CurrentUser = Depends(get_current_faculty),
) -> dict:
    # TODO(agent): Update Neo4j node properties.
    return {"status": "updated", "node_id": node_id}
