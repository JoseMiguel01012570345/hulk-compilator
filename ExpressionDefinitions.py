from EnumsExpressionDefinitions import ExpressionType
from ExpressionInterfaces import IExpression,Expression,InvalidExpression,ResolveExpressionException
from EnumsTokensDefinition import Operator
from TokensDefinition import OperatorToken
from ErrorsDefinition import SintaxError

class NumberExpression(IExpression,Expression):
    
    def __init__(self,expressions,operators):
        self._expressions = expressions
        self._operators = operators
        self._resolved = False
        self._value = 0
        pass
    
    @property
    def _Expressions(self):
        return self._expressions
    
    @property
    def Type(self):
        return ExpressionType.Number
    
    @property
    def Operators(self):
        return self._operators
    
    @property
    def Value(self):
        if not self._resolved:
            self.Resolve()
            self._resolved = True
            return self._value
        return self._value
    
    def _resolve(self,left_value,right_expression,operator):
        return operator.Resolve(left_value,right_expression.Value)
    
    def Resolve(self):
        self._expressions[0].Resolve()
        self._value = self._expressions[0].Value
        if not type(self._value) == int and not type(self._value) == float:
            raise ResolveExpressionException(f'No se puede aplicar el operador \'{self._operators[0]}\' al tipo {self._expressions[0].Type}')
        for i in range(len(self._operators)):
            self._value = self._resolve(self._value,self._expressions[i + 1],self._operators[i])
            pass
        pass
    
    def __add__(self,expression):
        if isinstance(expression,NumberExpression):
            return NumberExpression([self,expression],[OperatorToken('+')])
        raise ResolveExpressionException(f'No se puede aplicar el operador \'+\' al tipo {expression.Type}')
    
    def __sub__(self,expression):
        if isinstance(expression,NumberExpression):
            return NumberExpression([self,expression],[OperatorToken('-')])
        raise ResolveExpressionException(f'No se puede aplicar el operador \'-\' al tipo {expression.Type}')
        
    def __mul__(self,expression):
        if isinstance(expression,NumberExpression):
            return NumberExpression([self,expression],[OperatorToken('*')])
        raise ResolveExpressionException(f'No se puede aplicar el operador \'*\' al tipo {expression.Type}')
        
    def __truediv__(self,expression):
        if isinstance(expression,NumberExpression):
            return NumberExpression([self,expression],[OperatorToken('/')])
        raise ResolveExpressionException(f'No se puede aplicar el operador \'/\' al tipo {expression.Type}')
        
    def __pow__(self,expression):
        if isinstance(expression,NumberExpression):
            return NumberExpression([self,expression],[OperatorToken('^')])
        raise ResolveExpressionException(f'No se puede aplicar el operador \'^\' al tipo {expression.Type}')
        
    def __mod__(self,expression):
        if isinstance(expression,NumberExpression):
            return NumberExpression([self,expression],[OperatorToken('%')])
        raise ResolveExpressionException(f'No se puede aplicar el operador \'%\' al tipo {expression.Type}')
    
    def __str__(self):
        return str(self.Value)
    
    pass

class BooleanExpression(IExpression,Expression):
    
    def __init__(self,expressions,operators):
        self._expressions = expressions
        self._operators = operators
        self._resolved = False
        self._value = False
        pass
    
    @property
    def _Expressions(self):
        return self._expressions

    @property
    def Type(self):
        return ExpressionType.Boolean
    
    @property
    def Operators(self):
        return self._operators
    
    @property
    def Value(self):
        if not self._resolved:
            self.Resolve()
            self._resolved = True
            return self._value
        return self._value
    
    def _resolve(self,left_value,right_expression,operator):
        return operator.Resolve(left_value,right_expression.Value)
    
    def Resolve(self):
        self._expressions[0].Resolve()
        self._value = self._expressions[0].Value
        if not type(self._value) == bool:
            raise ResolveExpressionException(f'No se puede aplicar el operador \'{self._operators[0]}\' al tipo {self._expressions[0].Type}')
        for i in range(len(self._operators)):
            self._value = self._resolve(self._value,self._expressions[i + 1],self._operators[i])
            pass
        pass

    def __str__(self):
        return str(self.Value)
        
    pass

class StringExpression(IExpression,Expression):
    
    def __init__(self,expressions,operators):
        self._expressions = expressions
        self._operators = operators
        self._value = ''
        self._resolved = False
        pass
    
    @property
    def _Expresions(self):
        return self._expressions
    
    @property
    def Type(self):
        return ExpressionType.String
    
    @property
    def Operators(self):
        return self._operators
    
    @property
    def Value(self):
        if not self._resolved:
            self.Resolve()
            self._resolved = True
            return self._value
        return self._value
    
    def _resolve(self,left_value,right_expression,operator):
        return operator.Resolve(left_value,right_expression.Value)
          
    def Resolve(self):
        self._expressions[0].Resolve()
        self._value = self._expressions[0].Value
        if not type(self._value) == str:
            raise ResolveExpressionException(f'No se puede aplicar el operador \'@\' al tipo {self._expressions[0].Type}')
        
        for i in range(len(self._operators)):
            self._value = self._resolve(self._value,self._expressions[i + 1],self._operators[i])
            pass
        pass
    
    def __str__(self):
        return str(self.Value)
    
    pass