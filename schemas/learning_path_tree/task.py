from pydantic import BaseModel, Field
from schemas.learning_path_tree.task_type import TaskType

class Task(BaseModel):
    """A single practice task within a lesson."""
    id: str
    type: TaskType
    title: str
    instruction: str = Field(..., description="What the learner must do. Clear, specific.")
    starter_code: str | None = Field(None, description="Boilerplate to give them. None for quiz/reflect.")
    expected_behavior: str = Field(..., description="What correct completion looks like. Used by Evaluator Agent.")
    hints: list[str] = Field(default_factory=list, description="Progressive hints. First is vague, last near-answer.")
    language: str | None = Field(None, description="e.g. python, javascript, sql. None for non-code tasks.")
