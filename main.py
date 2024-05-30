from Lexer import Lexer
from RegExDefinitions import TokenConstrainedRegEx,TokenFinitRegEx
from TokensDefinition import KeywordToken,SimbolToken,OperatorToken,VariableToken,LiteralToken,Type
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES,SIMBOL_VALUES,OPERATOR_VALUES
from Rules import LiteralBooleanRule,LiteralNumericRule,LiteralStringRule,NameVariableRule
from ExpressionDefinitions import NumberExpression,StringExpression,BooleanExpression
from VariableDefinitions import NumberVariable,StringVariable,BooleanVariable
from LiteralDefinitions import NumberLiteral,StringLiteral,BooleanLiteral
import GRAMMAR_PRODUCTIONS
import Parser as P
from os import system
from CIL import ASTCilBuilder
import semantic_errors

def FiltToken(token):
    return len(token.Text) > 0

#_____________________________LEXER___________________________________________________

# build automaton to recognice language

keyword_token_recognizer = TokenFinitRegEx(KEYWORD_VALUES,KeywordToken)

simbol_token_recognizer = TokenFinitRegEx(SIMBOL_VALUES,SimbolToken)

operator_token_recognizer = TokenFinitRegEx(OPERATOR_VALUES,OperatorToken)

variable_token_recognizer = TokenConstrainedRegEx([NameVariableRule()],VariableToken)

boolean_literal_token_recognizer = TokenConstrainedRegEx([LiteralBooleanRule()],LiteralToken,Type.Boolean)

numeric_literal_token_recognizer = TokenConstrainedRegEx([LiteralNumericRule()],LiteralToken,Type.Number)

string_literal_token_recognizer = TokenConstrainedRegEx([LiteralStringRule()],LiteralToken,Type.String)

print('+++++++++++++++++++++ TokeniZING ++++++++++++++++++++++++++++++')

# save to priority dictionary

recognizers = {
    0: keyword_token_recognizer,
    1: simbol_token_recognizer,
    2: operator_token_recognizer,
    3: boolean_literal_token_recognizer,
    4: numeric_literal_token_recognizer,
    5: string_literal_token_recognizer,
    6: variable_token_recognizer
}

# start lexer with defined rules

lexer = Lexer(recognizers)

system("cls")

# load code
reader = open('TestCode.hk','r')
code = reader.read()
lexer.LoadCode(code)

# check for lexical errors
Error = False
my_list =[]

for state in lexer.LexicalAnalisys(lexer.Tokenize(),FiltToken):
    
    my_list = my_list.__add__(state.TokensSequence)
    
    if state.Error != None:
        
        Error =True
        print(state)
        
        break
    pass

#__________________PARSER__________________________________________
# go to parse
if not Error:
    
    tokens = [token for token in my_list if token.Text != '\n' and token.Text != ' ']
    
    my_list = tokens
    
    #------------PRINTS_TOKEN_SEQUENCE----------------
    # zz=[]
    # for item in my_list:
    #     zz.append(item.Text)
    
    # for t in my_list:
    #     print(t)
    #     pass
    #----------------------------
    
    gp =P.Parser(GRAMMAR_PRODUCTIONS.grammar , my_list )

    # if gp.derivation_Tree == None: 
        
    #     print(" \033[1;32m >\033[1;31m CODE HAS ERRORS :( \033[0m")

#_________________________SEMANTIC CHEKING__________________________________

    # gp.derivation_Tree.parent_reference()

    # gp.derivation_Tree.send_context()
    
    # context_error = semantic_errors.context_errors()
    
    # error_list = gp.derivation_Tree.context_check([])
    
    # context_error.add_error(error_list)
    
    # context_error.print_()
    
#_________________________CODE GENERATION__________________________________

    
    # AST = ASTCilBuilder(gp.derivation_Tree)
    
    # print(AST.Code)

    pass
#________________________END_____________________________________________