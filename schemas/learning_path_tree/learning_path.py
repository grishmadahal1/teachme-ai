from pydantic import BaseModel, Field
from schemas.learning_path_tree.difficulty_level import DifficultyLevel
from schemas.learning_path_tree.module import Module
from schemas.learner_input.learner_intent import LearnerIntent

class LearningPath(BaseModel):
    """
    The full output of the Planner Agent.
    A structured, ordered curriculum tree ready to be rendered and executed.
    """
    id: str
    title: str
    summary: str = Field(..., description="2-3 sentence overview of what the learner will achieve.")
    difficulty: DifficultyLevel
    total_estimated_hours: float
    modules: list[Module] = Field(..., min_length=1)

    # Metadata the rest of the system uses
    language: str | None = Field(None, description="Primary programming language, if any.")
    tags: list[str] = Field(default_factory=list)
    intent: LearnerIntent  # Echo back the input so we have full context

    # Adaptive signals (populated by Evaluator over time, empty at creation)
    weak_areas: list[str] = Field(default_factory=list)
    completed_lesson_ids: list[str] = Field(default_factory=list)
    current_lesson_id: str | None = None