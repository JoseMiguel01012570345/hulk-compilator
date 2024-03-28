class IExpressionParser:
    
    def Parse(self,tokens):
        """
        Parse() -> Expression
        parsea una cadena de tokens
        """
        raise NotImplementedError()
    
    pass

class IShiftReduceParser(IExpressionParser):
    
    def Shift(self):
        """
        se desplaza en la cadena
        """
        raise NotImplementedError()
    
    def Reduce(self):
        """
        reduce el token actual
        """
        raise NotImplementedError()
    
    pass