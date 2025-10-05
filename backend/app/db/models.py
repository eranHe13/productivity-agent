from sqlalchemy import Column, Integer, String, DateTime , Boolean , ForeignKey , String , Date
from app.db.session import Base
from datetime import datetime
from sqlalchemy.orm import relationship



class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    color = Column(String, nullable=True)

    tasks = relationship("Task" , back_populates="category" , cascade="all, delete-orphan")    



class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)
    due_date = Column(DateTime , nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category" , back_populates="tasks")

class DailyGoal(Base):
    __tablename__ = "daily_goals"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=datetime.today, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)


class FocusSession(Base):
    __tablename__ = "focus_sessions"

    id = Column(Integer, primary_key=True, index=True)
    start_ts = Column(DateTime, default=datetime.now)
    end_ts = Column(DateTime, nullable=True)
    duration_sec = Column(Integer, nullable=True)
    type = Column(String, nullable=True)
    interrupted = Column(Boolean, default=False)



class CoachPrompt(Base):
    __tablename__ = "coach_prompts"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=True)
    ts = Column(DateTime, default=datetime.now)
    model = Column(String, nullable=True)
    tokens_in = Column(Integer, default=0)
    tokens_out = Column(Integer, default=0)