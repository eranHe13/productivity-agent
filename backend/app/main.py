from fastapi import FastAPI
from app.db.session import Base, engine
from app.api.router import router
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Productivity Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"}
