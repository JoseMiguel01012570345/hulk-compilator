from EnumErrorTypes import ErrorType

class ERROR:
    
    def __init__(self,message,column,line):
        self._message = message
        self._column = column
        self._line = line
        pass
    
    @property
    def Message(self):
        return self._message
    
    @property
    def Column(self):
        return self._column
    
    @property
    def Line(self):
        return self._line
    
    @property
    def Type(self):
        """
        Type() -> ErrorType
        devuelve el tipo del error obtenido
        """
        
        raise NotImplementedError()
    
    def __str__(self):
        return f'{self.Type} ERROR en la linea {self.Line} columna {self.Column}: {self._message}'
    
    pass

class LexicalError(ERROR):
    
    def __init__(self,message,column,line):
        super().__init__(message,column,line)
        pass
    
    @property
    def Type(self):
        return ErrorType.LEXICAL
    
    pass

class SemanticError(ERROR):
    
    def __init__(self,message,column,line):
        super().__init__(message,column,line)
        pass
    
    @property
    def Type(self):
        return ErrorType.SEMANTIC
    
    pass

class SintaxError(ERROR):
    
    def __init__(self,message,column,line):
        super().__init__(message,column,line)
        pass
    
    @property
    def Type(self):
        return ErrorType.SINTAX
    
    pass