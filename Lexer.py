from RegExDefinitions import TokenFinitRegEx,TokenConstrainedRegEx,IRegEx,State
from TokensDefinition import KeywordToken,OperatorToken,SimbolToken,VariableToken,LiteralToken,EndToken
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES,OPERATOR_VALUES,SIMBOL_VALUES
from EnumsTokensDefinition import Type,TokenType,Simbol
from copy import copy
from ErrorsDefinition import LexicalError
from CodeStatesDefinition import CompilationStateERROR,CompilationStateOK

class Lexer(IRegEx):
    """
    automata que reconoce todas las cadenas que pertenecen al lenguaje definido
    """
    
    def __init__(self,recognizers):
        """
        recognizers -> dict<int,IRegEx>
        diccionario de los automatas que reconoceran nuestro lenguaje, las llaves son las prioridades de cada automata
        """
        self._recognizers = recognizers
        self._priorities = list(self._recognizers.keys())
        # ordenamos de menor a mayor las prioridades
        for i in range(len(self._priorities)):
            for j in range(i,len(self._priorities)):
                if self._priorities[j] < self._priorities[i]:
                    temp = self._priorities[i]
                    self._priorities[i] = self._priorities[j]
                    self._priorities[j] = temp
                    pass
                pass
            pass
        
        # creamos cada uno de los automatas correspondientes a los diferentes tipos de token
        
        # los guardamos en una lista
        
        # establecemos las variables de control
        self._text_readed = ''
        self._match = False
        self._state = State.START
        self._last_state = State.START
        self._reading_string = False
        self.Code = ''
        self._error = None
        pass

    @property
    def Error(self):
        return self._error
    
    @property
    def Expression(self):
        return self._text_readed
    
    @property
    def Match(self):
        return self._match
    
    @property
    def State(self):
        return self._state
    
    @property
    def LastState(self):
        return self._last_state
    
    @property
    def Token(self):
        
        # ya que la lista de prioridades esta ordenada, larecorremos para ver quien reconocio la cadena
        for value in self._priorities:
            if self._recognizers[value].LastState == State.FINAL:
                return self._recognizers[value].Token
            pass
        # si nadie la reconocio
        self._state = State.FAULT
        # retornamos lo que sea que haya leido el automata de menos prioridad
        return self._recognizers[len(self._recognizers.keys()) - 1]
    
    def LoadCode(self,code):
        self.Code = code
        pass
    
    def Restart(self):
        self._text_readed = ''
        self._match = False
        self._state = State.START
        self._last_state = State.START
        for recognizer in self._recognizers.values():
            recognizer.Restart()
            pass
        pass
    
    def Forward(self,character):
        self._last_state = copy(self.State)
            
        # intentamos reconocer la cadena de alguna forma
        forward = False
        fault = True
        
        for recognizer in self._recognizers.values():
            
            if not self._reading_string and recognizer.Type == Type.String:
                continue
        
            forward = recognizer.Forward(character) or forward
            
            if not recognizer.State == State.FAULT:
                fault = False
                pass
            
            if recognizer.State == State.FINAL:
                self._state = State.FINAL
                self._match = True
                pass
        
            pass
        
        if not forward or fault:
            self._state = State.FAULT
            self._error = self._recognizers[len(self._recognizers) - 1].Error
            pass
        else:
            self._text_readed += character
            self._match = False
            if not self._state == State.FINAL:
                self._state = State.ONWORK
                pass
            pass
        
        return forward and not fault
    
    def Tokenize(self):
        # mientras que haya codigo que leer
        while len(self.Code) > 0:
            position = 0
            # mientras que alguno de los automatas haya tenido transicion
            while self.Forward(self.Code[position]):
                # quitamos el caracter leido
                position += 1
                if len(self.Code) - 1 < position: break
                pass
                
            # si estamos en un estado final
            if self.LastState == State.FINAL:
                # retornamos el token encontrado
                
                yield self.Token
                # comprabmos si estamos leyendo un string
                if self._text_readed == '"' and not self._reading_string:
                    self._reading_string = True
                    pass
                elif self._text_readed == '"':
                    self._reading_string = False
                    pass
                
                self.Restart()
                self.Code = self.Code[position:]
                if position == 0: self.Code = self.Code[1:]
                
                pass
            
            pass
            
            yield EndToken('')
        
        pass
    
    def LexicalAnalisys(self,tokens,filter):
        """
        Este metodo comprueba las reglas de escritura de los tokens definidos por el lenguaje
        """
        last_token =  None
        current_token = None
        
        line = 1
        column = 1
        
        instruction = []
        
        tokens_filtered = []
        for token in tokens:
            if filter(token):
                tokens_filtered.append(token)
                pass
            pass
        
        for token in tokens_filtered:
            
            last_token = copy(current_token)
            current_token = token
            
            instruction.append(token)
            
            if not last_token == None and token.Type == TokenType.Variable and last_token.Type == TokenType.Literal and last_token.SelfType == Type.Number:
                error = LexicalError(self._error.Message,column,line)
                yield CompilationStateERROR(error)
                break
            
            if token.Type == TokenType.Simbol:
                if token.Simbol == Simbol.JumpLine or token.Simbol == Simbol.PointCom:
                    yield CompilationStateOK(instruction)
                    instruction.clear()
                    pass
                pass
            
            if token.Type == TokenType.Simbol and token.Simbol == Simbol.JumpLine:
                line += 1
                column = 1
                pass
            else:
                column += len(token.Text)
                pass
            
            pass
        
        pass
    
    pass