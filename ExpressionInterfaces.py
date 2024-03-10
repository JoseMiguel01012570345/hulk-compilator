from EnumsExpressionDefinitions import ExpressionType

class IExpression:
    
    @property
    def Value(self):
        """
        devuelve el valor de la expresion que representa
        """
        
        raise NotImplementedError()
    
    def Resolve(self):
        """
        computa el valor de la expresion que representa
        debe ser sobreescrito por las clases que hereden de ella
        """
        
        pass
    
    pass

class Expression:
    
    @property
    def Type(self):
        """
        Type() -> ExpressionType
        devuelve el tipo de la expression que representa
        """
        
        raise NotImplementedError()
    
    @property
    def Operators(self):
        """
        Operators() -> OperatorToken[]
        devuelve una lista con los operadores incluidos en dicha expresion
        """
        
        raise NotImplementedError()
    
    pass

class InvalidExpression(Expression):
    
    def __init__(self,error):
        self._error = error
        pass
    
    @property
    def ExpressionError(self):
        """
        ExpressionError() -> Error
        devuelve el error de dicha expression
        """
        
        return self._error
    
    @property
    def Type(self):
        return ExpressionType.Invalid
    
    def __str__(self):
        return str(self._error)
    
    pass

class ResolveExpressionException(Exception):

    def __init__(self,message):
        super().__init__(message)
        self.message = message
        pass

    pass