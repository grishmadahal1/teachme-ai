from enum import Enum

class Pace(str, Enum):
    relaxed = "relaxed"       # ~1-2 hrs/week
    steady  = "steady"        # ~3-5 hrs/week
    intense = "intense"       # ~10+ hrs/week
