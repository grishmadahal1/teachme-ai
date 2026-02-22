from pydantic import BaseModel, Field
from schemas.learning_path_tree.lesson import Lesson

class Module(BaseModel):
    """A cluster of related lessons around a theme."""
    id: str
    title: str
    description: str
    lessons: list[Lesson] = Field(..., min_length=1)
    estimated_hours: float
