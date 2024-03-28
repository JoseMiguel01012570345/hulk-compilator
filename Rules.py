from HULK_LANGUAGE_DEFINITION import SIMBOL_VALUES,OPERATOR_VALUES
import re

class Rule:
    """
    clase que define a una regla
    """
    
    def __init__(self,function):
        """
        function() -> bool
        """
        self._function = function
        pass
    
    @property
    def Description(self):
        """
        descripcion de la regla
        """
        
        raise NotImplementedError()
    
    def Try(self,value):
        """
        retorna True si cumple parcialmente la regla
        """
        
        return self._function(value)
    
    def Final(self,value):
        """
        retorna True si es cumple completamente la regla
        """
        
        raise NotImplementedError()
        
    pass

def BooleanRule(value):
    return 'true'.startswith(value) or 'false'.startswith(value) or value == 'true' or value == 'false'

def VariableRule(name):
    
    if name[0].isnumeric():
        return False
    
    if not name.isalnum():
        for simbol in SIMBOL_VALUES:
            if len(simbol) == 1 and name.count(simbol) > 0:
                return False
            pass
        for operator in OPERATOR_VALUES:
            if len(operator) == 1 and name.count(operator) > 0:
                return False
            pass
        return True
    
    return True

def NumericRule(number):
    
    if len(number) == 0:
        return False
    
    if number.count('-') > 1 or number.count('+') > 1: return False
    
    if number.count('.') > 1: return False
    
    if number.count('e') > 1: return False
    
    ignore = ['e','+','-','.']
    n = ''
    
    for char in number:
        if ignore.count(char) == 0:
            n += char
            pass
        pass
    
    if not n.isnumeric(): return False
    
    return True

def StringRule(string):
    return string.count('"') == 0

class LiteralStringRule(Rule):
    
    def __init__(self):
        super().__init__(StringRule)
        pass
    
    @property
    def Description(self):
        return 'Las cadenas de texto no pueden contener el caracter \'"\''
    
    def Final(self,value):
        return True
    
    pass

class LiteralBooleanRule(Rule):
    
    def __init__(self):
        super().__init__(BooleanRule)
        pass
    
    @property
    def Description(self):
        return 'Los valores solo pueden ser \'true\' o \'false\''
    
    def Final(self,value):
        return value == 'false' or value == 'true'
    
    pass

class NameVariableRule(Rule):
    
    def __init__(self):
        super().__init__(VariableRule)
        pass
    
    @property
    def Description(self):
        return 'Los nombres de variables deben comenzar con una letra y no pueden contener operadores o simbolos reservados por el lenguaje'
    
    def Final(self,value):
        return True
    
    pass

class LiteralNumericRule(Rule):
    
    def __init__(self):
        super().__init__(NumericRule)
        
        self._ex1 = '[1-9_][0-9_]*'
        self._ex2 = '[0-9_]*[.][0-9_]*[1-9_]'
        self._ex3 = '[1-9_][0-9_]*e[+,-][1-9_][0-9_]*'
        
        pass
    
    @property
    def Description(self):
        return 'Los numeros solo deben seguir estas reglas: [1-9][0-9]...[1-9].[0-9]...[0-9] ; 0.[0-9]...[0-9] o [1-9][0-9]...[1-9]e< + o - >[1-9][0-9]...[1-9]'
    
    
    def Final(self,value):
        
        if len(value) == 1 and value.isnumeric():
            return True
        
        t1 = re.findall(self._ex1,value)
        if not len(t1) == 1:
            
            t1 = re.findall(self._ex2,value)
            
            if not len(t1) == 1:
                
                return len(re.findall(self._ex3,value)) == 1
        
            return True
        
        return True
    
    pass