from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import CurrentUser, get_current_faculty, get_current_student
from app.models.submission import AppealStatus, Submission
from app.schemas.submissions import AppealRequest, SubmissionCreateRequest, SubmissionResponse

router = APIRouter()


@router.post("/assignments/{assignment_id}/submit", response_model=SubmissionResponse)
async def submit_assignment(
    assignment_id: UUID,
    body: SubmissionCreateRequest,
    student: CurrentUser = Depends(get_current_student),
    db: AsyncSession = Depends(get_db),
) -> Submission:
    # Count existing attempts
    result = await db.execute(
        select(Submission).where(
            Submission.assignment_id == assignment_id,
            Submission.student_id == student.id,
        )
    )
    existing = result.scalars().all()

    submission = Submission(
        assignment_id=assignment_id,
        student_id=student.id,
        content=body.content,
        content_json=body.content_json,
        attempt_number=len(existing) + 1,
    )
    db.add(submission)
    await db.flush()

    # TODO(agent): Trigger GraderAgent async:
    #   1. Load assignment rubric + source material
    #   2. Call GraderAgent.evaluate(submission, rubric, sources)
    #   3. Update submission with ai_grade, feedback, xp_awarded, gold_awarded
    #   4. Trigger GameAgent to update student XP/Gold/streak/badges
    #   For now, return the ungraded submission

    return submission


@router.post("/submissions/{submission_id}/appeal")
async def appeal_grade(
    submission_id: UUID,
    body: AppealRequest,
    student: CurrentUser = Depends(get_current_student),
    db: AsyncSession = Depends(get_db),
) -> dict:
    result = await db.execute(select(Submission).where(Submission.id == submission_id))
    submission = result.scalar_one_or_none()
    if not submission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Submission not found")
    if submission.student_id != student.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not your submission")

    submission.appeal_status = AppealStatus.PENDING
    await db.flush()
    return {"status": "appeal_submitted", "submission_id": str(submission_id)}


@router.get("/submissions/{submission_id}/ai-rationale")
async def get_ai_rationale(
    submission_id: UUID,
    faculty: CurrentUser = Depends(get_current_faculty),
    db: AsyncSession = Depends(get_db),
) -> dict:
    result = await db.execute(select(Submission).where(Submission.id == submission_id))
    submission = result.scalar_one_or_none()
    if not submission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Submission not found")
    return {
        "submission_id": str(submission_id),
        "ai_grade": submission.ai_grade,
        "feedback": submission.feedback,
    }
