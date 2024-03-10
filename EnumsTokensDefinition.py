from enum import Enum

class TokenType(Enum):

    Operator = 0
    Simbol = 1
    Keyword = 2
    Variable = 3
    Literal = 4

    pass

class Keyword(Enum):

    Print = 0
    Let = 1
    Function = 2
    In = 3
    Protocol = 4
    Type = 5
    New = 6
    If = 7
    Else = 8
    Elif = 9
    While = 10
    For = 11
    Cos = 12
    Sin = 13
    Tan = 14
    Log = 15
    Exp = 16
    Sqrt = 17
    Rand = 18
    Range = 19
    Euler = 20
    PI = 21
    Inherits = 22
    NONE = 23

    pass

class KeywordType(Enum):

    Function = 0
    Conditional = 1
    Loop = 2
    Declarator = 3
    Const = 4

    pass

class Simbol(Enum):

    LeftP = 0
    RightP = 1
    LeftB = 2
    RightB = 3
    Com = 4
    Point = 5
    PointCom = 6
    DoublePoint = 7
    RightArrow = 8
    DoubleCom = 9
    SimpleCom = 10
    WhiteSpace = 11
    End = 12
    Start = 13
    Self = 14
    JumpLine = 15
    NONE = 16

    pass

class SimbolType(Enum):
    
    Agrupator = 0
    Separator = 1
    Accesor = 2
    Declarator = 3

    pass

class Operator(Enum):
    
    Plus = 0
    PPlus = 1
    Minus = 2
    MMinus = 3
    Mul = 4
    Div = 5
    Exp = 6
    Rest = 7
    LessThan = 8
    GreatherThan = 9
    Eq = 10
    DoubleEq = 11
    DoublePointEq = 12
    LessEqThan = 13
    GreatherEqThan = 14
    Distint = 15
    And = 16
    Or = 17
    Not = 18
    Ask = 19
    Concat = 20
    Is = 21
    As = 22
    NONE = 23

    pass

class OperatorType(Enum):

    Unary = 0
    Binary = 1
    Ternary = 2

    pass

class Type(Enum):
    
    Number = 0
    String = 1
    Boolean = 2
    Object = 3
    Defined = 4
    NONE = 5

    pass

# Variables staticas locales
KEYWORDS_DICT = {
    'print' : Keyword.Print,
    'let' : Keyword.Let,
    'function' : Keyword.Function,
    'in' : Keyword.In,
    'protocol' : Keyword.Protocol,
    'type' : Keyword.Type,
    'new' : Keyword.New,
    'if' : Keyword.If,
    'else' : Keyword.Else,
    'elif' : Keyword.Elif,
    'while' : Keyword.While,
    'for' : Keyword.For,
    'cos' : Keyword.Cos,
    'sin' : Keyword.Sin,
    'tan' : Keyword.Tan,
    'log' : Keyword.Log,
    'exp' : Keyword.Exp,
    'sqrt' : Keyword.Sqrt,
    'rand' : Keyword.Rand,
    'range' : Keyword.Range,
    'E' : Keyword.Euler,
    'PI' : Keyword.PI,
    '' : Keyword.NONE
}

SIMBOLS_DICT = {
    '(' : Simbol.LeftP,
    ')' : Simbol.RightP,
    '{' : Simbol.LeftB,
    '}' : Simbol.RightB,
    ',' : Simbol.Com,
    '.' : Simbol.Point,
    ';' : Simbol.PointCom,
    ':' : Simbol.DoublePoint,
    '=>' : Simbol.RightArrow,
    '\"' : Simbol.DoubleCom,
    '\'' : Simbol.SimpleCom,
    ' ' : Simbol.WhiteSpace,
    '' : Simbol.End,
    'self' : Simbol.Self,
    '\n' : Simbol.JumpLine,
    '❌' : Simbol.NONE
}

OPERATORS_DICT = {
    '+' : Operator.Plus,
    '++' : Operator.PPlus,
    '-' : Operator.Minus,
    '--' : Operator.MMinus,
    '*' : Operator.Mul,
    '/' : Operator.Div,
    '^' : Operator.Exp,
    '%' : Operator.Rest,
    '<' : Operator.LessThan,
    '>' : Operator.GreatherThan,
    '=' : Operator.Eq,
    '==' : Operator.DoubleEq,
    ':=' : Operator.DoublePointEq,
    '<=' : Operator.LessEqThan,
    '>=' : Operator.GreatherEqThan,
    '!=' : Operator.Distint,
    '&' : Operator.And,
    '|' : Operator.Or,
    '!' : Operator.Not,
    '?' : Operator.Ask,
    '@' : Operator.Concat,
    'is' : Operator.Is,
    'as' : Operator.As,
    '' : Operator.NONE
}

TYPES_DICT = {
    'number' :Type.Number,
    'string' :Type.String,
    'boolean' :Type.Boolean,
    'object' :Type.Object,
    '' :Type.NONE
}