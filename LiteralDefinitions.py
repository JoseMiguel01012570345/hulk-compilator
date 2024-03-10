from ExpressionDefinitions import NumberExpression,BooleanExpression,StringExpression

class ILiteral:
    
    @property
    def Value(self):
        """
        devuelve el valor del literal que representa
        """
        raise NotImplementedError()
    
    pass

class NumberLiteral(ILiteral,NumberExpression):
    
    def __init__(self,value):
        if not type(value) == float and not type(value) == int:
            raise Exception('El valor asignado debe ser un valor numerico')
        self._value = value
        pass
    
    @property
    def Value(self):
        return self._value
    
    def Resolve(self):
        pass
    
    def __str__(self):
        return str(self._value)
    
    pass

class BooleanLiteral(ILiteral,BooleanExpression):
    
    def __init__(self,value):
        if not type(value) == bool:
            raise Exception('El valor asignado debe ser un valor booleano')
        self._value = value
        pass
    
    @property
    def Value(self):
        return self._value
    
    def Resolve(self):
        pass
    
    def __str__(self):
        return str(self._value)
    
    pass
class StringLiteral(ILiteral,StringExpression):
    
    def __init__(self,value):
        if not type(value) == str:
            raise Exception('El valor asignado debe ser un string')
        self._value = value
        pass
    
    @property
    def Value(self):
        return self._value
    
    def Resolve(self):
        pass
    
    def __str__(self):
        return str(self.Value)
    
    pass