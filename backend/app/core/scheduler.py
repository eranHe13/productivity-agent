from datetime import datetime, timedelta

def schedule_next_task(tasks, current_time=None):
    current_time = current_time or datetime.now()
    # Basic logic for now
    upcoming = [t for t in tasks if t.due_date and t.due_date > current_time]
    return min(upcoming, key=lambda t: t.due_date, default=None)
