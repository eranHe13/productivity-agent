from fastapi import APIRouter
from app.api import tasks, categories, goals, focus, coach

router = APIRouter()
router.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
router.include_router(categories.router, prefix="/categories", tags=["Categories"])
router.include_router(goals.router, prefix="/goals", tags=["DailyGoals"])
router.include_router(focus.router, prefix="/focus", tags=["Focus"])
router.include_router(coach.router, prefix="/coach", tags=["Coach"])
