from enum import Enum

class ProductionType(Enum):
    
    T = 'terminal'
    N = 'no terminal'
    E = 'epsilon'
    
    pass

class Grammar:
    
    """
    class that defines a grammar
    """
    
    def __init__(self,NonTerminals,Terminals,Productions,StartSimbol):
        """
        NonTerminals, Terminals: lists of Productions objects
        Productions: dict str,[str]
        StartSimbol: str
        """
        
        self._NonTerminals = NonTerminals
        self._Terminals = Terminals
        self._Productions = Productions
        self._StartSimbol = StartSimbol
        pass
    
    def Reduce(self,expression):
        """
        reduce an expression to it's productor
        """
        
        for production in self._Productions.keys():
            if self._Productions[production].count(expression) > 0:
                return production
            pass
        
        return None
    
    def GetProductions(self,expression):
        """
        returns the productions of a expression
        """
        
        if list(self._Productions.keys()).count(expression) == 0:
            return []
        
        return self._Productions[expression]

    @property
    def Productions(self):
        """
        returns all the productions of this grammar
        """
        
        result = []
        for production in self._Productions.keys():
            result = result.__add__(self._Productions[production])
            pass
        return result
    
    def Type(self,expression):
        """
        return true if an expression is terminal
        """
        
        if self._NonTerminals.count(expression) > 0:
            return ProductionType.N
        if self._Terminals.count(expression) > 0:
            return ProductionType.T
        return ProductionType.E
    
    def IsSentenceForm(self,expression):
        """
        return true if the expression ends in a terminal
        """
        if len(expression) == 0:
            return True
        for token in expression:
            if not self._NonTerminals.count(token) > 0 and not self._Terminals.count(token) > 0:
                raise Exception(f'El token {token} no existe en esta gramatica')
            pass
        return True
    
    def IsSentence(self,expression):
        """
        return true if the expression ends in a terminal
        """
        return self.Type(expression[len(expression) - 1]) == ProductionType.T
    
    def DeriveEpsilon(self,expression):
        """
        return true if the expression derive in epsilon
        """
        for production in self.GetProductions(expression):
            if self.Type(production) == ProductionType.E:
                return True
            if self.DeriveEpsilon(production):
                return True
            pass
        return False
    
    def First(self,expression):
        """
        return the First's set of the given expression
        """
        
        for i in range(len(expression) + 1):
            x = expression[:i]
            Z = expression[i:]
            
            if self.IsSentenceForm(Z) and self.IsSentenceForm(expression) and self.Type(x) == ProductionType.T and len(x) > 0:
                return [x]
            pass
        
        result = []
        
        for production in self.GetProductions(expression):
            first = self.First(production)
            for prefix in first:
                if result.count(prefix) == 0:
                    result.append(prefix)
                    pass
                pass
            pass
        
        if self.DeriveEpsilon(expression):
            if result.count('') == 0:
                result.append('')
                pass
            pass
        
        for i in range(len(expression)):
            Y = expression[:i]
            Z = expression[i:]
            
            if self.IsSentenceForm(expression) and self.IsSentenceForm(Z) and self.Type(Y) == ProductionType.N:
                first = self.First(Y)
                for prefix in first:
                    if result.count(prefix) == 0:
                        result.append(prefix)
                        pass
                    pass
                pass
            
            if self.DeriveEpsilon(Y):
                first = self.First(Z)
                for prefix in first:
                    if result.count(prefix) == 0:
                        result.append(prefix)
                        pass
                    pass
                pass
            
            pass
        
        return result
    
    def Follow(self,expression):
        """
        returns the Follow's set of the given expression
        """
        result = []
        
        if expression == self._StartSimbol:
            result.append('$')
            pass
        
        for i in range(len(expression) + 1):
            W = expression[:i]
            AZ = expression[i:]
            
            for j in range(len(AZ) + 1):
                A = AZ[:j]
                Z = AZ[j:]
                
                if self.IsSentenceForm(W) and self.IsSentenceForm(Z) and self.Type(A) == ProductionType.N:
                    first = self.First(Z)
                    for prefix in first:
                        if len(prefix) > 0:
                            result.append(prefix)
                            pass
                        pass
                    pass
                
                if self.DeriveEpsilon(Z):
                    follow = self.Follow(A)
                    for sufix in follow:
                        if len(sufix) > 0:
                            result.append(sufix)
                            pass
                        pass
                    pass
                pass
            pass

        return result
    
    pass