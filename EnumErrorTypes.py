from enum import Enum

class ErrorType(Enum):
    
    LEXICAL = 0
    SINTAX = 1
    SEMANTIC = 2
    UNDEFINED = 3
    NONE = 4
    
    pass