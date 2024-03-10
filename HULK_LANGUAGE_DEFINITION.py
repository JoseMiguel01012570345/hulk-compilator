from EnumsTokensDefinition import Keyword,Simbol,Operator
from OperatorResolvers import *
import json

"""
Aqui se define el conjunto de simbolos, operadores y palabras reservadas del lenguaje a interpretar
"""

# Variables globales del modulo
global KEYWORD_VALUES
global KEYWORD_FUNCTIONS
global KEYWORD_DECLARATORS
global KEYWORD_CONDITIONALS
global KEYWORD_LOOPS
global KEYWORD_CONSTS
global OPERATOR_VALUES
global OPERATOR_TEXTUALS
global SIMBOL_VALUES
global SIMBOL_TEXTUALS
global TYPES_DEFINED
global DEFINITION_PATH
global SIMBOL_ACCESORS
global SIMBOL_AGRUPATORS
global SIMBOL_SEPARATORS
global SIMBOL_DECLARATORS
global OPERATORS_UNARY
global OPERATORS_TERNARY
# Constantes del modulo
DEFINITION_PATH = 'LANGUAGE_DEFINITION.json'

def LoadDefinition():
    
    reader = open(DEFINITION_PATH,'r')
    definition = json.load(reader)
    # imprimimos la informacion cargada
    for key in definition.keys():
        print(key,definition[key])
        pass
    # cargamos todas las palabras claves
    for keyword in definition['keywords']:
        if KEYWORD_VALUES.count(keyword) == 0:
            KEYWORD_VALUES.append(keyword)
            pass
        pass
    # cargamos todos los simbolos
    for simbol in definition['simbols']:
        if SIMBOL_VALUES.count(simbol) == 0:
            SIMBOL_VALUES.append(simbol)
            pass
        pass
    # cargamos todos los operadores
    for operator in definition['operators']:
        if OPERATOR_VALUES.count(operator) == 0:
            OPERATOR_VALUES.append(operator)
            pass
        pass
    # cargamos todos los tipos
    for _type in definition['types']:
        if TYPES_DEFINED.count(_type) == 0:
            TYPES_DEFINED.append(_type)
            pass
        pass
    
    # actualizamos las demas definiciones
    for function in definition['keyword_functions']:
        if KEYWORD_FUNCTIONS.count(function) == 0:
            KEYWORD_FUNCTIONS.append(function)
            pass
        pass
    for declarator in definition['keyword_declarators']:
        if KEYWORD_DECLARATORS.count(declarator) == 0:
            KEYWORD_DECLARATORS.append(declarator)
            pass
        pass
    for conditional in definition['keyword_conditionals']:
        if KEYWORD_CONDITIONALS.count(conditional) == 0:
            KEYWORD_CONDITIONALS.append(conditional)
            pass
        pass
    for loop in definition['keyword_loops']:
        if KEYWORD_LOOPS.count(loop) == 0:
            KEYWORD_LOOPS.append(loop)
            pass
        pass
    for const in definition['keyword_consts']:
        if KEYWORD_CONSTS.count(const) == 0:
            KEYWORD_CONSTS.append(const)
            pass
        pass
    
    reader.close()
    pass

KEYWORD_VALUES = [
    'new',
    'print',
    'function',
    'let',
    'in',
    'protocol',
    'type',
    'while',
    'for',
    'if',
    'else',
    'elif',
    'cos',
    'sin',
    'tan',
    'log',
    'E',
    'PI',
    'exp',
    'sqrt',
    'rand',
    'range',
    'inherits'
]

KEYWORD_DICT = {
    'new' : Keyword.New,
    'print' : Keyword.Print,
    'function' : Keyword.Function,
    'let' : Keyword.Let,
    'in' : Keyword.In,
    'protocol' : Keyword.Protocol,
    'type' : Keyword.Type,
    'while' : Keyword.While,
    'for' : Keyword.For,
    'if' : Keyword.If,
    'else' : Keyword.Else,
    'elif' : Keyword.Elif,
    'cos' : Keyword.Cos,
    'sin' : Keyword.Sin,
    'tan' : Keyword.Tan,
    'log' : Keyword.Log,
    'E' : Keyword.Euler,
    'PI' : Keyword.PI,
    'exp' : Keyword.Exp,
    'sqrt' : Keyword.Sqrt,
    'rand' : Keyword.Rand,
    'range' : Keyword.Range,
    'inherits' : Keyword.Inherits
}

KEYWORD_FUNCTIONS = [
    'cos',
    'sin',
    'tan',
    'print',
    'exp',
    'sqrt',
    'rand',
    'range',
    'log'
]

KEYWORD_DECLARATORS = [
    'let',
    'in',
    'protocol',
    'type',
    'new'
]

KEYWORD_CONDITIONALS = [
    'if',
    'else',
    'elif'
]

KEYWORD_LOOPS = [
    'while',
    'for'
]

KEYWORD_CONSTS = [
    'PI',
    'E'    
]

OPERATOR_VALUES = [
    '+',
    '-',
    '*',
    '/',
    '^',
    '%',
    '<',
    '>',
    '<=',
    '>=',
    '=',
    '==',
    '@',
    '++',
    '--',
    ':=',
    '!',
    '?',
    '&',
    '|',
    '~',
    'is',
    'as'
]

OPERATOR_DICT = {
    '+' : Operator.Plus,
    '-' : Operator.Minus,
    '*' : Operator.Mul,
    '/' : Operator.Div,
    '^' : Operator.Exp,
    '%' : Operator.Rest,
    '<' : Operator.LessThan,
    '>' : Operator.GreatherThan,
    '<=' : Operator.LessEqThan,
    '>=' : Operator.GreatherEqThan,
    '=' : Operator.Eq,
    '==' : Operator.DoubleEq,
    '@': Operator.Concat,
    '++' : Operator.PPlus,
    '--' : Operator.MMinus,
    ':=' : Operator.DoublePointEq,
    '!' : Operator.Distint,
    '?' : Operator.Ask,
    '&' : Operator.And,
    '|' : Operator.Or,
    '~' : Operator.Not,
    'is' : Operator.Is,
    'as' : Operator.As
}

OPERATOR_TEXTUALS = [
    'is',
    'as'
]

OPERATORS_TERNARY = [
    '?'
]

OPERATORS_UNARY = [
    '!',
    '++',
    '--'
]

OPERATOR_RESOLVERS = {
    '+' : PlusOperatorResolver,
    '-' : MinusOperatorResolver,
    '*' : MulOperatorResolver,
    '/' : DivOperatorResolver,
    '^' : ExpOperatorResolver,
    '%' : RestOperatorResolver,
    '<' : LessThanOperatorResolver,
    '>' : GreatherThanOperatorResolver,
    '<=' : LessEqThanOperatorResolver,
    '>=' : GreatherEqThanOperatorResolver,
    '=' : EqOperatorResolver,
    '==' : DoubleEqOperatorResolver,
    '@': ConcatOperatorResolver,
    '++' : PPlusOperatorResolver,
    '--' : MMinusOperatorResolver,
    ':=' : DoublePointEqOperatorResolver,
    '!' : DistintOperatorResolver,
    '?' : AskOperatorResolver,
    '&' : AndOperatorResolver,
    '|' : OrOperatorResolver,
    '~' : NotOperatorResolver,
    'is' : IsOperatorResolver,
    'as' : AsOperatorResolver
}

SIMBOL_VALUES = [
    "(",
    ")", 
    "{",
    "}",
    ".",
    "=>",
    "\"",
    " ",
    ";",
    ",",
    "\n",
    "self",
    ":",
    ""
]

SIMBOL_DICT = {
    "(" : Simbol.LeftP,
    ")" : Simbol.RightP, 
    "{" : Simbol.LeftB,
    "}" : Simbol.RightB,
    "." : Simbol.Point,
    "=>" : Simbol.RightArrow,
    "\"" : Simbol.DoubleCom,
    " " : Simbol.WhiteSpace,
    ";" : Simbol.PointCom,
    "," : Simbol.Com,
    "\n" : Simbol.JumpLine,
    "self" : Simbol.Self,
    ":" : Simbol.DoublePoint,
    "" : Simbol.End
}

SIMBOL_TEXTUALS = [
    'self'
]

SIMBOL_ACCESORS = [
    '.',
    'self'
]

SIMBOL_AGRUPATORS = [
    '(',
    ')',
    '{',
    '}'
]

SIMBOL_DECLARATORS = [
    '=>',
    '\"',
    ':'
]

SIMBOL_SEPARATORS = [
    ',',
    '\n',
    ';'
]

TYPES_DEFINED = [
    'object',
    'number',
    'boolean',
    'string'
]

LoadDefinition()