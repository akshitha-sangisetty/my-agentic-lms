"""
Assignment publishing service — manages status transitions.
"""

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession


async def publish_assignment(assignment_id: UUID, db: AsyncSession) -> None:
    """Transition assignment from FACULTY_REVIEW to PUBLISHED."""
    # TODO(agent): Implement publish logic:
    #   1. Validate assignment has rubric
    #   2. Validate concept_tags are non-empty
    #   3. Update status to PUBLISHED
    #   4. Emit assignment.published event
    pass
