"""
Assignment generation service — orchestrates the DesignerAgent.
"""

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession


async def generate_assignments(
    course_id: UUID,
    config: dict,
    db: AsyncSession,
) -> list[dict]:
    """Generate assignments by calling the DesignerAgent.

    Steps:
    1. Load Knowledge Graph for the course from Neo4j
    2. Load course config (gamification level, strictness)
    3. Call DesignerAgent with KG + config
    4. Validate generated assignments
    5. Store in DB with status=FACULTY_REVIEW
    """
    # TODO(agent): Implement assignment generation pipeline.
    #   See packages/agents/agents/designer/ for the DesignerAgent.
    return []
