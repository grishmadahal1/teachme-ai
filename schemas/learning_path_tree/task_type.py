from enum import Enum

class TaskType(str, Enum):
    code        = "code"         # Write/fix code in the editor
    quiz        = "quiz"         # Multiple choice or short answer
    debug       = "debug"        # Given broken code, fix it
    build       = "build"        # Mini project, open-ended
    reflect     = "reflect"      # Written explanation (tests understanding, not syntax)
