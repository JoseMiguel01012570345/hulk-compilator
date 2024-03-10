from Token import Token
from Utils import isNumeric
from TokenInterfaces import IKeywordToken,ILiteralToken,ISimbolToken,IOperatorToken,IVariableToken
from EnumsTokensDefinition import Keyword,KeywordType,Type,Operator,OperatorType,TokenType,Simbol,SimbolType,OPERATORS_DICT,KEYWORDS_DICT,SIMBOLS_DICT
from HULK_LANGUAGE_DEFINITION import KEYWORD_CONDITIONALS,KEYWORD_DECLARATORS,KEYWORD_FUNCTIONS,KEYWORD_LOOPS,KEYWORD_VALUES,OPERATORS_UNARY,OPERATORS_TERNARY,SIMBOL_AGRUPATORS,SIMBOL_ACCESORS,SIMBOL_DECLARATORS,SIMBOL_VALUES,OPERATOR_VALUES,OPERATOR_RESOLVERS

class KeywordToken(Token,IKeywordToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        if KEYWORD_VALUES.count(Text) == 0:
            raise Exception('Token no definido')
        pass
    
    @property
    def Type(self):
        """
        Type() -> TokenType
        devuelve el tipo de token que representa
        """
        
        return TokenType.Keyword
    
    @property
    def Keyword(self):
        """
        Keyword() -> Keyword
        devuelve la palabra reservada que representa
        """
               
        return KEYWORDS_DICT[self.Text]

    @property
    def KeywordType(self):
        """
        KeywordType() -> KeywordType
        devuelve el tipo de palabra reservada que representa
        """
        
        if KEYWORD_FUNCTIONS.__contains__(self.Text):
            return KeywordType.Function
        if KEYWORD_DECLARATORS.__contains__(self.Text):
            return KeywordType.Declarator
        if KEYWORD_CONDITIONALS.__contains__(self.Text):
            return KeywordType.Conditional
        if KEYWORD_LOOPS.__contains__(self.Text):
            return KeywordType.Loop
        return KeywordType.Const
        
    pass

class LiteralToken(Token,ILiteralToken):
    
    def __init__(self,Text,self_type):
        super().__init__(Text)
        self._self_type = self_type
        pass
    
    @property
    def Type(self):
        """
        Type() -> Type
        devuelve el tipo de token que representa
        """
        
        return TokenType.Literal
    
    @property
    def SelfType(self):
        """
        SelfType() -> Type
        devuelve el tipo del valor del token que representa
        """
        
        return self._self_type
    
    pass

class OperatorToken(Token,IOperatorToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        if OPERATOR_VALUES.count(Text) == 0:
            raise Exception('Token no definido')
        pass
    
    @property
    def Type(self):
        """
        Type() -> TokenType
        devuelve el tipo de token que representa
        """
        
        return TokenType.Operator
    
    @property
    def Operator(self):
        """
        Operator() -> Operator
        devuelve el operador que representa
        """
        
        return OPERATORS_DICT[self.Text]

    @property
    def OperatorType(self):
        """
        OperatorType() -> OperatorType
        devuelve el tipo de operador que representa
        """
        
        if OPERATORS_UNARY.count(self.Text) > 0:
            return OperatorType.Unary
        if OPERATORS_TERNARY.count(self.Text) > 0:
            return OperatorType.Ternary
        return OperatorType.Binary
    
    @property
    def Resolve(self):
        return OPERATOR_RESOLVERS[self.Text]
    
    pass

class SimbolToken(Token,ISimbolToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        if SIMBOL_VALUES.count(Text) == 0:
            raise Exception('Token no definido')
        pass
    
    @property
    def Type(self):
        """
        Type() -> TokenType
        devuelve el tipo del token que representa
        """
        
        return TokenType.Simbol
    
    @property
    def Simbol(self):
        """
        Simbol() -> Simbol
        devuelve el simbolo que representa
        """
        return SIMBOLS_DICT[self.Text]
    
    @property
    def SimbolType(self):
        """
        SimbolType() -> SimbolType
        devuelve el tipo de simbolo que representa
        """
        
        if SIMBOL_AGRUPATORS.count(self.Text) > 0:
            return SimbolType.Agrupator
        if SIMBOL_ACCESORS.count(self.Text) > 0:
            return SimbolType.Accesor
        if SIMBOL_DECLARATORS.count(self.Text):
            return SimbolType.Declarator
        return SimbolType.Separator
    
    pass

class VariableToken(Token,IVariableToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        pass
    
    @property
    def Type(self):
        """
        Type() -> TokenType
        devuelve el tipo del token que representa
        """
        
        return TokenType.Variable
    
    @property
    def Name(self):
        """
        Name() -> string
        devuelve el nombre de la variable que representa
        """

        return self.Text
    
    pass

class EndToken(SimbolToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        pass
    
    @property
    def Simbol(self):
        return Simbol.End
    
    @property
    def SimbolType(self):
        return SimbolType.Separator
    
    pass