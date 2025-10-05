import requests
import json
from datetime import datetime, timedelta

BASE_URL = "http://localhost:8000/api"

def check_health():
    r = requests.get("http://localhost:8000/health")
    print("Health:", r.status_code, r.text)

def create_category():
    payload = {"name": "Testing", "color": "#FFAA00"}
    r = requests.post(f"{BASE_URL}/categories/", json=payload)
    print("Create category:", r.status_code, r.text)
    if r.ok:
        return r.json()["id"]
    return None

def create_task(category_id=None):
    payload = {
        "title": "System check task",
        "completed": False,
        "due_date": (datetime.utcnow() + timedelta(days=1)).isoformat(),
        "category_id": category_id
    }
    r = requests.post(f"{BASE_URL}/tasks/", json=payload)
    print("Create task:", r.status_code, r.text)
    if r.ok:
        return r.json()["id"]
    return None

def list_tasks():
    r = requests.get(f"{BASE_URL}/tasks")
    print("List tasks:", r.status_code, len(r.json()) if r.ok else r.text)

def mark_done(task_id):
    r = requests.post(f"{BASE_URL}/tasks/{task_id}/done")
    print("Mark task done:", r.status_code, r.text)

def create_goal():
    payload = {"date": datetime.utcnow().date().isoformat(), "title": "Daily goal check", "completed": False}
    r = requests.post(f"{BASE_URL}/goals/today/", json=payload)
    print("Create goal:", r.status_code, r.text)

def start_focus():
    r = requests.post(f"{BASE_URL}/focus/start")
    print("Start focus:", r.status_code, r.text)
    if r.ok:
        return r.json()["session_id"]
    return None

def stop_focus(session_id):
    r = requests.post(f"{BASE_URL}/focus/stop", params={"session_id": session_id})
    print("Stop focus:", r.status_code, r.text)

def ask_coach():
    payload = {"prompt": "Summarize system health in one line."}
    r = requests.post(f"{BASE_URL}/coach/", json=payload)
    print("Coach:", r.status_code)
    if r.ok:
        print(r.json()["answer"][:120], "...")
    else:
        print(r.text)

def main():
    print("\n=== SYSTEM CHECK START ===")
    check_health()

    cat_id = create_category()
    task_id = create_task(cat_id)
    list_tasks()
    if task_id:
        mark_done(task_id)
    create_goal()

    sid = start_focus()
    if sid:
        stop_focus(sid)

    ask_coach()

    print("=== SYSTEM CHECK COMPLETE ===")

if __name__ == "__main__":
    main()
