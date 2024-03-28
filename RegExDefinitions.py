from RegExInterface import State,IRegEx
from ErrorsDefinition import LexicalError
from copy import copy
class TokenFinitRegEx(IRegEx):
    """
    clase que reconoce tokens que pertenezcan a un conjunto finito
    """

    def __init__(self,valid_values,token_creator):
        """
        values -> list(str)
        valores admisibles
        token_creator -> Constructor de la clase que instanciara los tokens
        """
        self._match = False
        self._text_readed = ''
        self._state = State.START
        self._last_state = State.START
        self._values = valid_values
        self._creator = token_creator
        self._error = None
        self._column = 1
        self._line = 1
        pass
    
    @property
    def Type(self):
        return None
    
    @property
    def Error(self):
        return self._error
    
    @property
    def Match(self):
        return self._match
    
    @property
    def Expression(self):
        return self._text_readed
    
    @property
    def State(self):
        return self._state
    
    @property
    def LastState(self):
        return self._last_state

    @property
    def Token(self):
        return self._creator(self._text_readed)
    
    def Restart(self):
        self._match = False
        self._state = State.START
        self._text_readed = ''
        self._last_state = State.START
        pass
    
    def Forward(self,character):
        self._last_state = copy(self._state)
        
        if character == '\n':
            self._line += 1
            self._column = 1
            pass
        else:
            self._column += 1
            pass
        
        if self._state == State.FAULT:
            return False
        
        if len(character) == 0:
            return True
        
        for value in self._values:
            if value.startswith(self._text_readed + character):
                self._text_readed += character
                if len(value) == len(self._text_readed):
                    self._state = State.FINAL
                    self._match = True
                    pass
                else:
                    self._state = State.ONWORK
                    self._match = False
                    pass
                return True
            pass
        self._match = False
        self._state = State.FAULT
        self._error = LexicalError(f'La cadena \'{self._text_readed}\' no es una cadena valida del lenguaje',self._column,self._line)
        return False
    
    pass

class TokenConstrainedRegEx(IRegEx):
    
    def __init__(self,constrains,token_creator,self_type=None):
        """
        constrains -> instancias de la clase Rule
        restricciones que debe cumplir el token
        token_creator -> constructor de la clase de token que reconocera
        """
        self._match = False
        self._state = State.START
        self._last_state = State.START
        self._text_readed = ''
        self._constrains = constrains
        self._creator = token_creator
        self._self_type = self_type
        self._error = None
        self._column = 1
        self._line = 1
        pass
    
    @property
    def Type(self):
        return self._self_type
    
    @property
    def Error(self):
        return self._error
    
    @property
    def Match(self):
        return self._match
    
    @property
    def Expression(self):
        return self._text_readed
    
    @property
    def State(self):
        return self._state
    
    @property
    def LastState(self):
        return self._last_state

    @property
    def Token(self):
        if self._self_type == None:
            if not self._state == State.FINAL:
                return self._creator(self._text_readed[:len(self._text_readed) - 1])
            return self._creator(self._text_readed)
        if not self._state == State.FINAL:
            return self._creator(self._text_readed[:len(self._text_readed) - 1],self._self_type)
        return self._creator(self._text_readed,self._self_type)
    
    def Restart(self):
        self._state = State.START
        self._match = False
        self._text_readed = ''
        self._last_state = State.START
        pass
    
    def Forward(self,character):
        self._last_state = copy(self._state)
        
        if character == '\n':
            self._line += 1
            self._column = 1
            pass
        else:
            self._column += 1
            pass
         
        if len(character) == 0:
            return True
        
        for constrain in self._constrains:
            if not constrain.Try(self._text_readed + character):
                self._match = False
                self._state = State.FAULT
                self._error = LexicalError(constrain.Description,self._column,self._line)
                self._text_readed += character
                return False
            if constrain.Final(self._text_readed + character):
                self._state = State.FINAL
                pass
            pass
        
        # if self._state == State.FAULT:
        #     return False
                
        self._text_readed += character
        self._match = True
        if not self._state == State.FINAL:
            self._state = State.ONWORK
            pass
        
        return True
    
    pass