from EnumsTokensDefinition import TokenType,Type
import production_class_representation as pcr

'''

NOTE: every builder must return a list in where it specify the properties of the node

'''

def plus(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]

def minus(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]
    
def multiplier(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]

def divition(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]

def var(token_list):
    
    if token_list[0].Type == TokenType.Variable:
        return [ ( "name" , token_list[0].Text ) , ("value", None ) ]
    else:
        return literal(token_list)
    
def brackets(token_list):
    return [("expression",token_list[1])]

def replacement(token_list):
    return [( "replacement" , token_list[0])]

def let(token_list):
    return [ ( "name",token_list[1].name ) , ( "value" , token_list[-1] ) ]

def literal(token_list):
    return [ ( "value" , token_list[0].Text) , ( "id" , "literal" ) ]

def re_asigment(token_list):    
    return [ ( "name" , token_list[0].name ) , ("value", token_list[-1] ) ] 

def block(token_list):
    
    if not  token_list[0].__dict__.__contains__("id")  :
        return [ ( "expressions" , [token_list[1]] ) ]
    else:
        token_list[0].expressions.append(token_list[-1])
        
        return [ ( "expressions" , token_list[0].expressions  )  ]
        
def def_function(token_list):
    return [ ( "args" , token_list[-2] ) , ( "body", token_list[-1] ) ]

def in_(token_list):
    return [ ( "args" , token_list[0] ) , ( "body" , token_list[1] ) ]

def structure(token_list):
    
    if len(token_list) == 2:
        
        if token_list[-1].__dict__.__contains__("id"):
    
            token_list[0].expressions.append(token_list[1])
            return [ ("expressions", token_list[0] ) ]
    
        else:
            return [ ("expressions", token_list[0] ) ]
    
    if len(token_list) == 3 and token_list[0].__dict__.__contains__("id"):
        return [ ("expressions", token_list[1] ) ]

def params(token_list):
    return [( "replacement" , token_list[1])]
    
    