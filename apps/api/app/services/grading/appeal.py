"""
Appeal workflow service — handles student grade appeals.
"""

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession


async def submit_appeal(submission_id: UUID, reason: str, db: AsyncSession) -> None:
    """Submit a grade appeal — routes to faculty review queue."""
    # TODO(agent): Implement appeal workflow:
    #   1. Set submission.appeal_status = PENDING
    #   2. Notify faculty via event
    #   3. Log appeal with reason
    pass


async def review_appeal(
    submission_id: UUID, faculty_id: UUID, override_grade: dict | None, db: AsyncSession
) -> None:
    """Faculty reviews an appeal and optionally overrides the AI grade."""
    # TODO(agent): Implement appeal review:
    #   1. Store human_override with faculty rationale
    #   2. Update appeal_status to REVIEWED or OVERTURNED
    #   3. If overturned, recalculate XP/Gold via GameAgent
    pass
