from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import CurrentUser, get_current_student
from app.models.badge import Badge
from app.models.user import User
from app.schemas.gamification import (
    BadgeResponse,
    HintPreviewResponse,
    HintPurchaseRequest,
    HintPurchaseResponse,
    LeaderboardResponse,
    StudentProfileResponse,
)

router = APIRouter()


@router.get("/students/me/profile", response_model=StudentProfileResponse)
async def get_my_profile(
    student: CurrentUser = Depends(get_current_student),
    db: AsyncSession = Depends(get_db),
) -> User:
    result = await db.execute(select(User).where(User.id == student.id))
    return result.scalar_one()


@router.get("/courses/{course_id}/leaderboard", response_model=LeaderboardResponse)
async def get_leaderboard(
    course_id: UUID,
    student: CurrentUser = Depends(get_current_student),
) -> LeaderboardResponse:
    # TODO(agent): Implement Valkey sorted set leaderboard.
    #   Use ZREVRANGE for top entries, ZREVRANK for student's rank.
    #   Key: f"leaderboard:{course_id}"
    return LeaderboardResponse(course_id=course_id, entries=[], my_rank=None)


@router.get("/assignments/{assignment_id}/hint/preview", response_model=HintPreviewResponse)
async def preview_hint(
    assignment_id: UUID,
    tier: str = "NUDGE",
    student: CurrentUser = Depends(get_current_student),
    db: AsyncSession = Depends(get_db),
) -> HintPreviewResponse:
    # TODO(agent): Calculate dynamic hint price based on attempt count + gold balance.
    tier_costs = {"NUDGE": 10, "GUIDANCE": 30, "SOLUTION": 75}
    cost = tier_costs.get(tier, 10)

    result = await db.execute(select(User).where(User.id == student.id))
    user = result.scalar_one()

    return HintPreviewResponse(
        tier=tier,
        gold_cost=cost,
        current_balance=user.gold_balance,
        can_afford=user.gold_balance >= cost,
    )


@router.post("/assignments/{assignment_id}/hint", response_model=HintPurchaseResponse)
async def purchase_hint(
    assignment_id: UUID,
    body: HintPurchaseRequest,
    student: CurrentUser = Depends(get_current_student),
    db: AsyncSession = Depends(get_db),
) -> HintPurchaseResponse:
    # TODO(agent): Implement full hint purchase flow:
    #   1. Calculate cost (static or dynamic pricing)
    #   2. Check gold balance
    #   3. Call TutorAgent to generate hint at the requested tier
    #   4. Deduct gold, create HintTransaction
    #   5. Return hint text + new balance
    result = await db.execute(select(User).where(User.id == student.id))
    user = result.scalar_one()

    tier_costs = {"NUDGE": 10, "GUIDANCE": 30, "SOLUTION": 75}
    cost = tier_costs.get(body.tier, 10)

    if user.gold_balance < cost:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail=f"Insufficient gold. Need {cost}, have {user.gold_balance}.",
        )

    user.gold_balance -= cost
    await db.flush()

    return HintPurchaseResponse(
        hint_text="Hint generation not yet implemented. Check back soon!",
        gold_cost=cost,
        new_balance=user.gold_balance,
        tier=body.tier,
    )


@router.post("/students/me/streak-freeze")
async def purchase_streak_freeze(
    student: CurrentUser = Depends(get_current_student),
    db: AsyncSession = Depends(get_db),
) -> dict:
    result = await db.execute(select(User).where(User.id == student.id))
    user = result.scalar_one()
    cost = 100
    if user.gold_balance < cost:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail=f"Insufficient gold. Streak freeze costs {cost} Gold.",
        )
    user.gold_balance -= cost
    await db.flush()
    return {"status": "streak_freeze_purchased", "new_balance": user.gold_balance}


@router.get("/students/me/badges", response_model=list[BadgeResponse])
async def get_my_badges(
    student: CurrentUser = Depends(get_current_student),
    db: AsyncSession = Depends(get_db),
) -> list[Badge]:
    result = await db.execute(
        select(Badge).where(Badge.student_id == student.id).order_by(Badge.created_at.desc())
    )
    return list(result.scalars().all())
