from Lexer import Lexer
from RegExDefinitions import TokenConstrainedRegEx,TokenFinitRegEx
from TokensDefinition import KeywordToken,SimbolToken,OperatorToken,VariableToken,LiteralToken,Type
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES,SIMBOL_VALUES,OPERATOR_VALUES
from Rules import LiteralBooleanRule,LiteralNumericRule,LiteralStringRule,NameVariableRule
from ExpressionDefinitions import NumberExpression,StringExpression,BooleanExpression
from VariableDefinitions import NumberVariable,StringVariable,BooleanVariable
from LiteralDefinitions import NumberLiteral,StringLiteral,BooleanLiteral

def FiltToken(token):
    return len(token.Text) > 0

# creamos cada uno de los automatas que reconoceran nuestro lenguaje
keyword_token_recognizer = TokenFinitRegEx(KEYWORD_VALUES,KeywordToken)
simbol_token_recognizer = TokenFinitRegEx(SIMBOL_VALUES,SimbolToken)
operator_token_recognizer = TokenFinitRegEx(OPERATOR_VALUES,OperatorToken)
variable_token_recognizer = TokenConstrainedRegEx([NameVariableRule()],VariableToken)
boolean_literal_token_recognizer = TokenConstrainedRegEx([LiteralBooleanRule()],LiteralToken,Type.Boolean)
numeric_literal_token_recognizer = TokenConstrainedRegEx([LiteralNumericRule()],LiteralToken,Type.Number)
string_literal_token_recognizer = TokenConstrainedRegEx([LiteralStringRule()],LiteralToken,Type.String)

print('+++++++++++++++++++++ Tokenizando ++++++++++++++++++++++++++++++')
# los guardamos en el diccionario de prioridades
recognizers = {
    0: keyword_token_recognizer,
    1: simbol_token_recognizer,
    2: operator_token_recognizer,
    3: boolean_literal_token_recognizer,
    4: numeric_literal_token_recognizer,
    5: string_literal_token_recognizer,
    6: variable_token_recognizer
}

# instanciamos el lexer con las reglas definidas
lexer = Lexer(recognizers)

# cargamos el codigo
reader = open('TestCode.hk','r')
code = reader.read()
lexer.LoadCode(code)

# extraemos los tokens del codigo
for state in lexer.LexicalAnalisys(lexer.Tokenize(),FiltToken):
    print(state)
    pass


print('++++++++++++++++++++++ Computando +++++++++++++++++++++++')
# Ejemplos de como usar las expresiones
# Numericas
a = NumberLiteral(10)
b = NumberLiteral(5)

c = NumberVariable('Suma',(a - b).Value)

exp = NumberExpression([c ** b,a / c],[OperatorToken('^')])
print(exp.Value)

exp = a + b * (c ** b) - c + b/a
print(exp.Value)

# Mismos ejemplos para los demas tipos