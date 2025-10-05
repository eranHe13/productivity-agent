from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.db import models
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/start")
def start_focus(type: str = "work", db: Session = Depends(get_db)):
    session = models.FocusSession(start_ts=datetime.utcnow(), type=type)
    db.add(session)
    db.commit()
    db.refresh(session)
    return {"session_id": session.id, "start_ts": session.start_ts}


@router.post("/stop")
def stop_focus(session_id: int, db: Session = Depends(get_db)):
    session = db.query(models.FocusSession).get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    session.end_ts = datetime.utcnow()
    session.duration_sec = int((session.end_ts - session.start_ts).total_seconds())
    db.commit()
    return {"session_id": session.id, "duration_sec": session.duration_sec}
