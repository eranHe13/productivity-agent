import time
from fastapi import HTTPException

class RateLimiter:
    def __init__(self, limit_per_minute: int = 5):
        self.limit = limit_per_minute
        self.calls = []

    def check(self, user_id: str = "default"):
        now = time.time()
        window = 60
        # Save only calls from the last minute
        self.calls = [c for c in self.calls if now - c < window]
        if len(self.calls) >= self.limit:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        self.calls.append(now)

rate_limiter = RateLimiter(limit_per_minute=5)
