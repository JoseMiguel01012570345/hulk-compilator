class State:
    
    def __init__(self,error):
        self._error = error
        pass
    
    @property
    def Error(self):
        return self._error
    
    
    @property
    def TokensSequence(self):
        """
        TokensSequence() -> Tokens
        devuelve una lista de tuplas (token,line,column) para procesar la instruccion dada
        """
        
        raise NotImplementedError()
    
    def __str__(self):
        if self._error == None:
            return 'OK'
        return str(self._error)
    
    pass

class CompilationStateOK(State):
    
    def __init__(self,tokens=None):
        super().__init__(None)
        self._tokens = tokens
        pass
    
    @property
    def TokensSequence(self):
        return self._tokens
    
    pass

class CompilationStateERROR(State):
    
    def __init__(self,error):
        super().__init__(error)
        pass
    
    @property
    def TokensSequence(self):
        return []
    
    pass