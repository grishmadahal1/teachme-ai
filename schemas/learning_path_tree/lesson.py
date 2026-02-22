from pydantic import BaseModel, Field
from schemas.learning_path_tree.task import Task

class Lesson(BaseModel):
    """One focused learning unit. Should take 15-30 mins."""
    id: str
    title: str
    objective: str = Field(..., description="Single clear learning objective. Starts with a verb.")
    concepts: list[str] = Field(..., description="Key concepts introduced in this lesson.")
    prerequisite_lesson_ids: list[str] = Field(default_factory=list)
    tasks: list[Task] = Field(..., min_length=1)
    estimated_minutes: int
