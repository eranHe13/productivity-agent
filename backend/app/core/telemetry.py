import datetime
from app.db.session import SessionLocal
from app.db.models import FocusSession

def log_event(event_type: str, message: str):
    """Save a general log to the database or file"""
    ts = datetime.datetime.utcnow()
    print(f"[{ts}] {event_type}: {message}")

def log_focus_end(session_id: int):
    db = SessionLocal()
    session = db.query(FocusSession).get(session_id)
    if session:
        duration = int((session.end_ts - session.start_ts).total_seconds())
        log_event("FOCUS_END", f"Session {session_id} ended, {duration}s")
    db.close()
