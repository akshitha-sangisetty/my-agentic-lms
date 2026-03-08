from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import CurrentUser, get_current_faculty, get_current_user
from app.models.assignment import Assignment, AssignmentStatus
from app.schemas.assignments import (
    AssignmentGenerationConfig,
    AssignmentGenerationResponse,
    AssignmentResponse,
    AssignmentUpdateRequest,
)

router = APIRouter()


@router.post(
    "/courses/{course_id}/generate-assignments",
    response_model=AssignmentGenerationResponse,
)
async def generate_assignments(
    course_id: UUID,
    config: AssignmentGenerationConfig,
    faculty: CurrentUser = Depends(get_current_faculty),
    db: AsyncSession = Depends(get_db),
) -> AssignmentGenerationResponse:
    # TODO(agent): Call DesignerAgent to generate assignments from Knowledge Graph.
    #   1. Load Knowledge Graph for course from Neo4j
    #   2. Pass to DesignerAgent with config (types, count, difficulty)
    #   3. Store generated assignments with status=FACULTY_REVIEW
    #   4. Return list of generated assignments
    return AssignmentGenerationResponse(
        course_id=course_id,
        generated_count=0,
        assignments=[],
    )


@router.get("/courses/{course_id}/assignments", response_model=list[AssignmentResponse])
async def list_assignments(
    course_id: UUID,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> list[Assignment]:
    query = select(Assignment).where(Assignment.course_id == course_id)
    if user.role == "student":
        query = query.where(Assignment.status == AssignmentStatus.PUBLISHED)
    result = await db.execute(query.order_by(Assignment.order_index))
    return list(result.scalars().all())


@router.get("/assignments/{assignment_id}", response_model=AssignmentResponse)
async def get_assignment(
    assignment_id: UUID,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Assignment:
    result = await db.execute(select(Assignment).where(Assignment.id == assignment_id))
    assignment = result.scalar_one_or_none()
    if not assignment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assignment not found")
    if user.role == "student" and assignment.status != AssignmentStatus.PUBLISHED:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assignment not found")
    return assignment


@router.patch("/assignments/{assignment_id}", response_model=AssignmentResponse)
async def update_assignment(
    assignment_id: UUID,
    body: AssignmentUpdateRequest,
    faculty: CurrentUser = Depends(get_current_faculty),
    db: AsyncSession = Depends(get_db),
) -> Assignment:
    result = await db.execute(select(Assignment).where(Assignment.id == assignment_id))
    assignment = result.scalar_one()
    for field, value in body.model_dump(exclude_unset=True).items():
        if field == "hint_config" and value is not None:
            setattr(assignment, field, value.model_dump())
        else:
            setattr(assignment, field, value)
    await db.flush()
    return assignment


@router.post("/assignments/{assignment_id}/publish", response_model=AssignmentResponse)
async def publish_assignment(
    assignment_id: UUID,
    faculty: CurrentUser = Depends(get_current_faculty),
    db: AsyncSession = Depends(get_db),
) -> Assignment:
    result = await db.execute(select(Assignment).where(Assignment.id == assignment_id))
    assignment = result.scalar_one()
    assignment.status = AssignmentStatus.PUBLISHED
    await db.flush()
    return assignment
