"""
Badge eligibility engine — checks and awards badges.
"""

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

BADGE_DEFINITIONS = [
    {"name": "First Steps", "description": "Complete your first assignment", "icon": "rocket", "category": "mastery"},
    {"name": "Perseverance", "description": "Retry an assignment after failing", "icon": "shield", "category": "perseverance"},
    {"name": "Perfect Score", "description": "Score 100% on an assignment", "icon": "star", "category": "mastery"},
    {"name": "Streak Master", "description": "Maintain a 7-day streak", "icon": "flame", "category": "perseverance"},
    {"name": "Streak Legend", "description": "Maintain a 30-day streak", "icon": "crown", "category": "perseverance"},
    {"name": "Hint-Free", "description": "Complete 5 assignments without hints", "icon": "brain", "category": "mastery"},
    {"name": "Gold Saver", "description": "Accumulate 500 Gold", "icon": "coins", "category": "mastery"},
]


async def check_badge_eligibility(student_id: UUID, db: AsyncSession) -> list[dict]:
    """Check if student has earned any new badges.

    Returns list of newly awarded badges.
    """
    # TODO(agent): Implement badge eligibility checks:
    #   1. Load student profile + submission history
    #   2. Check each badge definition's criteria
    #   3. Award new badges (avoid duplicates)
    #   4. Return newly awarded badges for UI notification
    return []
