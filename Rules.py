from HULK_LANGUAGE_DEFINITION import SIMBOL_VALUES,OPERATOR_VALUES

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
        return self._function(value)
        
    pass

def BooleanRule(value):
    return value == 'true' or value == 'false'

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

    if number[0] == '-' or number[0] == '+':
        return NumericRule(number[1:])
    
    if number[0] == '0':
        if len(number) == 1:
            return True
        return len(number) > 2 and number[1] == '.' and number[2:].isnumeric()
    
    if number.count('.') > 0:
        
        parts = number.split('.')
        
        if len(parts) > 2:
            return False
        return parts[0].isnumeric() and parts[1].isnumeric() 
    
    if number.count('e') == 1:
        
        parts = number.split('e')
        
        if len(parts) > 2:
            return False
        if parts[1].startswith('+') or parts[1].startswith('-'):
            return parts[1][1:].isnumeric() and parts[0].isnumeric()
        return False
    
    return number.isnumeric()

def StringRule(string):
    return string.count('"') == 0

class LiteralStringRule(Rule):
    
    def __init__(self):
        super().__init__(StringRule)
        pass
    
    @property
    def Description(self):
        return 'Las cadenas de texto no pueden contener el caracter \'"\''
    
    pass

class LiteralBooleanRule(Rule):
    
    def __init__(self):
        super().__init__(BooleanRule)
        pass
    
    @property
    def Description(self):
        return 'Los valores solo pueden ser \'true\' o \'false\''
    
    pass

class NameVariableRule(Rule):
    
    def __init__(self):
        super().__init__(VariableRule)
        pass
    
    @property
    def Description(self):
        return 'Los nombres de variables deben comenzar con una letra y no pueden contener operadores o simbolos reservados por el lenguaje'
    
    pass

class LiteralNumericRule(Rule):
    
    def __init__(self):
        super().__init__(NumericRule)
        pass
    
    @property
    def Description(self):
        return 'Los numeros solo deben seguir estas reglas: [1-9][0-9]...[1-9].[0-9]...[0-9] ; 0.[0-9]...[0-9] o [1-9][0-9]...[1-9]e< + o - >[1-9][0-9]...[1-9]'
    
    pass