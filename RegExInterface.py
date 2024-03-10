from enum import Enum

class State:
    
    START = 0
    ONWORK = 1
    FINAL = 2
    FAULT = 3
    
    pass

class IRegEx:
    """
    Implementacion de una expresion regular
    Funciona basada en un automata determinista finito
    """
    
    @property
    def Error(self):
        """
        devuelve el error que provoco que cayera al estado FAULT
        """
        
        raise NotImplementedError()
    
    @property
    def Expression(self):
        """
        devuelve la expresion contenida en el automata
        """
        
        raise NotImplementedError()
    
    @property
    def Match(self):
        """
        devuelve true si la expresion dada corresponde a la definida por esta expresion regular
        """
        
        raise NotImplementedError()
    
    def Forward(self,character):
        """
        consume el caracter dado y cambia de estado en caso de existir transicion
        devuelve True si hubo trancision
        """
        
        raise NotImplementedError()
    
    @property
    def State(self):
        """
        devuelve en que estado se encuentra el automata
        """
        
        raise NotImplementedError()
    
    @property
    def LastState(self):
        """
        devuelve el ultimo estado antes del estado actual
        """
        
        raise NotImplementedError()
    
    def Restart(self):
        """
        reinicia el automata
        """
        
        raise NotImplementedError()
    
    pass