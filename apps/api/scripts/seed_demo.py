import asyncio
import uuid
from sqlalchemy import select

from app.database import async_session_factory
from app.models.institution import Institution
from app.models.user import User, UserRole
from app.models.course import Course, CourseStatus, GamificationLevel, GradingStrictness
from app.models.assignment import Assignment, AssignmentType, AssignmentStatus, AssignmentSource

COURSE_ID = uuid.UUID("bc1c2a1d-81f4-4769-86bb-4bf987994039")

async def seed():
    async with async_session_factory() as db:
        # 1. Ensure Institution
        inst_res = await db.execute(select(Institution).limit(1))
        inst = inst_res.scalar_one_or_none()
        if not inst:
            inst = Institution(name="Default University", data_residency="US_EAST")
            db.add(inst)
            await db.flush()

        # 2. Ensure Faculty & Student
        fac_res = await db.execute(select(User).where(User.email == "demo.faculty@university.edu"))
        faculty = fac_res.scalar_one_or_none()
        if not faculty:
            faculty = User(
                institution_id=inst.id,
                email="demo.faculty@university.edu",
                full_name="Demo Faculty",
                role=UserRole.FACULTY,
            )
            db.add(faculty)
            await db.flush()

        stud_res = await db.execute(select(User).where(User.email == "demo.student@university.edu"))
        student = stud_res.scalar_one_or_none()
        if not student:
            student = User(
                institution_id=inst.id,
                email="demo.student@university.edu",
                full_name="Demo Student",
                role=UserRole.STUDENT,
                xp_total=250,
                gold_balance=500,
                current_streak=3,
                longest_streak=5,
            )
            db.add(student)
            await db.flush()
        else:
            student.xp_total = max(student.xp_total, 250)
            student.gold_balance = max(student.gold_balance, 500)
            student.current_streak = max(student.current_streak, 3)

        # 3. Ensure Course
        c_res = await db.execute(select(Course).where(Course.id == COURSE_ID))
        course = c_res.scalar_one_or_none()
        if not course:
            course = Course(
                id=COURSE_ID,
                institution_id=inst.id,
                faculty_id=faculty.id,
                title="Python Programming & Agentic Systems",
                description="Master core Python concepts, data structures, and autonomous AI agents with hands-on labs and Socratic tutoring.",
                gamification_level=GamificationLevel.HIGH,
                grading_strictness=GradingStrictness.MEDIUM,
                status=CourseStatus.ACTIVE,
                hints_enabled=True,
                leaderboard_visible=True,
                streak_tracking_active=True,
            )
            db.add(course)
            await db.flush()
        else:
            course.status = CourseStatus.ACTIVE

        # 4. Ensure Assignments
        a1_id = uuid.UUID("11111111-1111-1111-1111-111111111111")
        a1_res = await db.execute(select(Assignment).where(Assignment.id == a1_id))
        if not a1_res.scalar_one_or_none():
            db.add(Assignment(
                id=a1_id,
                course_id=course.id,
                title="Variables & Data Types Fundamentals",
                description="Test your understanding of immutable types, dynamic typing, and numeric operations.",
                type=AssignmentType.MCQ,
                generated_by=AssignmentSource.AI_AGENT,
                status=AssignmentStatus.PUBLISHED,
                concept_tags=["Variables & Data Types", "Operators & Expressions"],
                max_xp=50,
                max_gold=20,
                content={
                    "questions": [
                        {
                            "question": "Which of the following data types in Python is immutable?",
                            "options": ["list", "dict", "tuple", "set"],
                            "answer": 2,
                            "explanation": "Tuples are immutable sequence types in Python."
                        }
                    ]
                }
            ))

        a2_id = uuid.UUID("22222222-2222-2222-2222-222222222222")
        a2_res = await db.execute(select(Assignment).where(Assignment.id == a2_id))
        if not a2_res.scalar_one_or_none():
            db.add(Assignment(
                id=a2_id,
                course_id=course.id,
                title="Code Lab: String Reversal & Slicing",
                description="Write a function `reverse_words(s: str) -> str` that reverses the order of words in a sentence.",
                type=AssignmentType.CODE_LAB,
                generated_by=AssignmentSource.AI_AGENT,
                status=AssignmentStatus.PUBLISHED,
                concept_tags=["String Operations", "Functions"],
                max_xp=100,
                max_gold=50,
                content={
                    "starter_code": "def reverse_words(s: str) -> str:\n    # Return the words in reversed order\n    pass\n",
                    "test_cases": [
                        {"input": "hello world", "expected": "world hello"},
                        {"input": "agentic lms", "expected": "lms agentic"}
                    ]
                }
            ))

        await db.commit()
        print("Successfully seeded demo course and assignments!")

if __name__ == "__main__":
    asyncio.run(seed())
