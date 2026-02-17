from pydantic import BaseModel

class Submission(BaseModel):
    username: str
    problem: str
    result: str   # AC / WA / TLE
    topic: str