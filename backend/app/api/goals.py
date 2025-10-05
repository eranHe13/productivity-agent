from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from app.db import models, schemas
from app.db.session import SessionLocal

router = APIRouter(prefix="/today")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[schemas.DailyGoal])
def get_today_goals(db: Session = Depends(get_db)):
    return db.query(models.DailyGoal).filter(models.DailyGoal.date == date.today()).all()


@router.post("/", response_model=schemas.DailyGoal)
def create_goal(goal: schemas.DailyGoalBase, db: Session = Depends(get_db)):
    db_goal = models.DailyGoal(**goal.dict())
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal
