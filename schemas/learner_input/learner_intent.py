from pydantic import BaseModel, Field
from schemas.learner_input.pace import Pace

class LearnerIntent(BaseModel):
    """What the learner tells us before we generate their path."""
    topic: str = Field(..., description="What they want to learn. Raw, natural language.")
    goal: str = Field(..., description="Why they want to learn it. Job, project, curiosity?")
    background: str = Field(..., description="What they already know. Free text, self-reported.")
    pace: Pace = Field(..., description="How much time they can commit per week.")
    outcome: str = Field(..., description="What does success look like for them specifically?")
