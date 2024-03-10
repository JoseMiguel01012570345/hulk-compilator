from ExpressionInterfaces import IExpression,Expression
from ExpressionDefinitions import NumberExpression,BooleanExpression
class UnassignatedVariableException(Exception):
    
    def __init__(self,message):
        self._message = message
        super().__init__(message)
        pass
    
    pass
class IVariable:
    
    @property
    def Name(self):
        """
        devuelve el nombre de la variable
        """
        raise NotImplementedError()
    
    @property
    def Value(self):
        """
        devuelve el valor de la variable
        """
        raise NotImplementedError()
    
    @property
    def IsAssignated(self):
        """
        devuelve si una variable ya ha sido asignada o no
        """
        raise NotImplementedError()
    
    def setValue(self,value):
        """
        cambia el valor de la variable
        """
        raise NotImplementedError()
    
    pass
class NumberVariable(IVariable,NumberExpression):
    
    def __init__(self,name,value=None):
        self._name = name
        if value == None:
            self._isassignated = False
            self._value = 0
            pass
        else:
            if not type(value) == float and not type(value) == int:
                raise Exception('El valor pasado debe ser un valor numerico')
            self._isassignated = True
            self._value = value
            pass
        pass
    
    @property
    def Name(self):
        return self._name
    
    @property
    def Value(self):
        if not self._isassignated:
            raise UnassignatedVariableException('No se ha asignado un valor a esta variable')
        return self._value
    
    @property
    def IsAssignated(self):
        return self._isassignated
    
    
    def setValue(self,value):
        if not type(value) == float and not type(value) == int:
            raise Exception('El valor pasado debe ser un valor numerico')
        self._isassignated = True
        self._value = value
        pass
    
    def Resolve(self):
        pass
    
    def __str__(self):
        return str(self.Value)
    
    pass
class BooleanVariable(IVariable,BooleanExpression):
    
    def __init__(self,name,value=None):
        self._name = name
        if value == None:
            self._value = False
            self._isassignated = False
            pass
        else:
            if not type(value) == bool:
                raise Exception('El valor pasado debe ser un valor booleano')
            self._isassignated = True
            self._value = value
            pass
        pass
    
    @property
    def Name(self):
        return self._name
    
    @property
    def Value(self):
        if not self._isassignated:
            raise UnassignatedVariableException('No se ha asignado un valor a la variable')
        return self._value
    
    @property
    def IsAssignated(self):
        return self._isassignated
    
    def setValue(self,value):
        if not type(value) == bool:
            raise Exception('El valor asignado debe ser un valor booleano')
        self._value = value
        
    def Resolve(self):
        pass
    
    def __str__(self):
        return str(self.Value)
    
    pass
class StringVariable(IVariable,NumberExpression):
    
    def __init__(self,name,value=None):
        self._name = name
        if value == None:
            self._isassignated = False
            self._value = ''
            pass
        else:
            if not type(value) == str:
                raise Exception('El valor asignado debe ser un string')
            self._value = value
            self._isassignated = True
            pass
        pass
    
    @property
    def Name(self):
        return self._name
    
    @property
    def Value(self):
        if not self._isassignated:
            raise UnassignatedVariableException('No se ha asignado un valor a esta variable')
        return self._value
    
    @property
    def IsAssignated(self):
        return self._isassignated
    
    def setValue(self,value):
        if not type(value) == str:
            raise Exception('El valor asignado debe ser un string')
        self._value = value
        
    def Resolve(self):
        pass
    
    def __str__(self):
        return str(self.Value)
    
    pass
