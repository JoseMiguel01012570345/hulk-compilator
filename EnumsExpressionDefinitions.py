from enum import Enum

class ExpressionType(Enum):
    
    Object = 0,
    Boolean = 1,
    Number = 2,
    String = 3,
    Defined = 4,
    Invalid = 5
    
    pass