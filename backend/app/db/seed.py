from app.db.session import SessionLocal, Base, engine
from app.db.models import Category

def init_seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    default_categories = [
        {"name": "Personal", "color": "#FFD166"},
        {"name": "Work", "color": "#06D6A0"},
        {"name": "Learning", "color": "#118AB2"},
        {"name": "Health", "color": "#EF476F"},
    ]
    for c in default_categories:
        exists = db.query(Category).filter(Category.name == c["name"]).first()
        if not exists:
            db.add(Category(**c))
    db.commit()
    db.close()

if __name__ == "__main__":
    init_seed()
