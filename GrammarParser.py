from RegExDefinitions import TokenFinitRegEx
from RegExInterface import State,IRegEx
from GrammarInterface import Grammar
from ParserInterface import IShiftReduceParser
from copy import copy
<<<<<<< HEAD
from os import system

class GrammarParser(IRegEx,IShiftReduceParser):
    
    Tokens = []
    
    def __init__(self,automatons,grammar):
        self._automatons = automatons
        self._error = None
        self._expression = ''
        self._match = False
        self._state = State.START
        self._lastState = State.START
        self._shift = False
        self._reduce = False
        self._grammar = grammar
        self._stack = []
        self._maxPrefixLength = 0
        
        for production in self._grammar._Productions.keys():
            for p in self._grammar._Productions[production]:
                if len(p) > self._maxPrefixLength:
                    self._maxPrefixLength = len(p)
                    pass
                pass
            pass
        
        pass
        
=======

class GrammarParser(IRegEx,IShiftReduceParser):
    """
    clase encargada de parsear una gramatica
    """
    _automatons = {}
    _maxPrefixLength = 0
    _items = {}
    
    def __init__(self,grammar):

        self._grammar = grammar
        self._createAutomatons()
        self._error = None
        self._expression = None
        self._match = False
        self._state = State.START
        self._laststate = State.START
        self._stack = []
        self._position = 0
        pass
    
>>>>>>> 849d64d (translator moved from GrammarParser)
    @property
    def Error(self):
        return self._error
    
    @property
    def Match(self):
        return self._match
    
    @property
    def Expression(self):
        return self._expression
    
    @property
    def State(self):
        return self._state
    
    @property
    def LastState(self):
<<<<<<< HEAD
        return self._lastState
    
    def Reduce(self):
        
        init = len(self._stack) - self._maxPrefixLength
        for i in range(max(0,init),len(self._stack)):
            
            p = ''
            for j in range(i,len(self._stack)):
                p += self._stack[j]
            
                for production in self._grammar._Productions.keys():
                    if self._grammar._Productions[production].count(p) > 0:
                        return production,p
                    pass
            
                pass
            pass
        
        return None,None
    
    def Shift(self):
        pass
    
    def Forward(self,token):
        
        self._lastState = copy(self._state)
        if self.LastState == State.FINAL:
            self._reduce = True
            pass
        else:
            self._reduce = False
            pass
        
        forward = False
        
        for automaton in self._automatons.keys():
            forward = self._automatons[automaton].Forward(token) or forward
            if self._automatons[automaton].State == State.ONWORK:
                self._state = State.ONWORK
                self._expression = self._automatons[automaton].Expression
                self._shift = True
                
                for value in self._automatons[automaton]._values:
                    if (self._expression + '.') == value:
                        self._state = State.FINAL
                        break
                    pass
                
                pass
            
            pass
        
        if not self._reduce:
            self._shift = True
            pass
                    
        return forward
    

=======
        return self._laststate
    
    def _createAutomatons(self):
        
        for production in self._grammar._Productions.keys():
            
            items = []
            for derivation in self._grammar._Productions[production]:
                if len(derivation) > self._maxPrefixLength:
                    self._maxPrefixLength = len(derivation)
                    pass
                for i in range(len(derivation) + 1):
                    items.append(f'{derivation[:i]}.{derivation[i:]}')
                    pass
                pass
            
            automaton = TokenFinitRegEx(items,lambda token: token)
            self._automatons[production] = automaton
            self._items[production] = items
            pass
            
        pass
    
>>>>>>> 849d64d (translator moved from GrammarParser)
    def Restart(self):
        for automaton in self._automatons.keys():
            self._automatons[automaton].Restart()
            pass
<<<<<<< HEAD
        self._shift = False
        self._reduce = False
        self._state = State.START
        self._lastState = State.START
        pass
    
    def LoadTokens(self,tokens):
        
        for token in tokens:
            self.Tokens.append(token)
            pass
        
        pass
    
    def Parse(self):
        
        position = 0
        
        
        while len(self.Tokens) > 1:
                        
            while position < len(self.Tokens) and self.Forward(self.Tokens[position]):
                self._stack.append(self.Tokens[position])
                system('clear')
                print(self._stack)
                position += 1
                pass
            
            if self._reduce:
                self._expression = ''
                reduction,production = self.Reduce()
                
                tokens = self.Tokens[position:]

                for i in range(len(production)):
                    self._stack.pop()
                    system('clear')
                    print(self._stack)
                    pass
                                
                self.Tokens = [reduction].__add__(tokens)
                self.Restart()
                position = 0
                pass
            
            if self._shift:
                self.Restart()
                pass
            
            pass
        
        pass

    pass
=======
        self._laststate = State.START
        self._state = State.START
        pass
    
    @property
    def _shift(self):
        for i in range(max(0,len(self._stack) - self._maxPrefixLength),len(self._stack)):
            token = ''
            for j in range(i,len(self._stack)):
                token += self._stack[j]
                pass
            
            for production in self._items.keys():
                for s in self._items[production]:
                    if s.startswith(token):
                        state = s
                        follow = state.split('.')[1]
                        if len(follow) > 0 and self._position < len(self._expression): return True
                        pass
                    pass
                pass
            pass
        return False
    
    def Shift(self):
        pass
    
    @property
    def _reduce(self):
        # revisar este metodo
        for i in range(max(0,len(self._stack) - self._maxPrefixLength),len(self._stack)):
            token = ''
            for j in range(i,len(self._stack)):
                token += self._stack[j]
                pass
            
            for production in self._items.keys():
                for s in self._items[production]:
                    if s.startswith(token):
                        follow = s.split('.')[1]
                        if len(follow) > 0: return False
                    pass
                pass
            pass
        
        return True
    
    def Reduce(self):
        
        while self._reduce:
            
            stack_temp = []
            reduced = False
            for i in range(max(0,len(self._stack) - self._maxPrefixLength),len(self._stack)):
                token = ''
                
                for j in range(i,len(self._stack)):
                    token += self._stack[j]
                    pass
                
                while len(stack_temp) < len(token):
                    stack_temp.append(self._stack.pop())
                    pass
                
                for production in self._items.keys():
                    if self._items[production].count(token + '.') > 0:
                        token = production
                        self._stack.append(token)
                        reduced = True
                        break
                    pass
                
                if reduced: break
            
                while len(stack_temp) > 0:
                    self._stack.append(stack_temp.pop())
                    pass
                
                pass
            pass
        pass
    
    def Forward(self,token):
        
        self._laststate = copy(self._state)
  
        for i in range(len(self._stack) + 1):
            t = ''
            for j in range(i,len(self._stack)):
                t += self._stack[j]
                pass
            t += token
            
            for production in self._items.keys():
                for state in self._items[production]:
                    if state.startswith(t + '.'):
                        self._state = State.FINAL
                        self._stack.append(token)
                        return True
                    pass
                pass
        
        self._state = State.FAULT
        
        return False
    
    def Parse(self,tokens):
        
        self._position = 0
        self._expression = tokens
        
        while self._position < len(tokens) and self.Forward(tokens[self._position]):
            
            _reduce = self._reduce
            _shift = self._shift
            
            if _reduce and _shift:
                raise Exception('Esta gramatica no es LR(0)')
            
            if self._reduce:
                self.Reduce()
                pass
            else:
                self.Shift()
                pass
            self.Restart()
            self._position += 1
            pass
        pass
    
    pass
>>>>>>> 849d64d (translator moved from GrammarParser)
