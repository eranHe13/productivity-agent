import time
import threading
from datetime import datetime
from app.db.session import SessionLocal
from app.db.models import FocusSession

class FocusTimer:
    def __init__(self, duration_min=25, type="work"):
        self.duration_sec = duration_min * 60
        self.type = type
        self._thread = None
        self._stop_event = threading.Event()
        self.session_id = None

    def start(self):
        db = SessionLocal()
        session = FocusSession(start_ts=datetime.utcnow(), type=self.type)
        db.add(session)
        db.commit()
        db.refresh(session)
        self.session_id = session.id
        db.close()

        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run)
        self._thread.start()
        return self.session_id

    def _run(self):
        start = time.time()
        while not self._stop_event.is_set():
            elapsed = time.time() - start
            if elapsed >= self.duration_sec:
                self.stop()
                break
            time.sleep(1)

    def stop(self):
        db = SessionLocal()
        session = db.query(FocusSession).get(self.session_id)
        if session:
            session.end_ts = datetime.utcnow()
            session.duration_sec = int((session.end_ts - session.start_ts).total_seconds())
            db.commit()
        db.close()
        self._stop_event.set()
        return session.duration_sec if session else 0
