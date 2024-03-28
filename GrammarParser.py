from RegExDefinitions import TokenFinitRegEx
from RegExInterface import State,IRegEx
from ParserInterface import IShiftReduceParser

class GrammarParser(IRegEx,IShiftReduceParser):
    """
    clase encargada de parsear una gramatica
    
    """
    operator_procedence =[
        
        ['^','%'],
        ['*','/'],
        ['+','-'],
        ['>','<','>=','<=','==','is'],
        ['&','||','!'],
        ['=','+=','-=','/=','*=','--',':='],
        ['if',"for",'W'],
        ["P ''"],
        ["X '"],
        ['@','@@'],
        ['.'],
        ['as'],
        ['let'],
        [',']
        ['type' , 'new' , 'function', 'in' , 'protocol' ,  ]
        [';']
        ['$']
    ]
    
    def __init__(self,grammar):

        self._grammar = grammar
        self._error = None
        self._match = False
        self._stack = []
        pass
    
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
        return self._laststate
    
    def Restart(self):        
        pass
    
    def compare_procedence(self , operator1 , operator2):
        
        '''
        campare operator1 precedence to operator2 procedence
        
        return values: 
        
        0: equal procedence
        1: grater procedence
        -1: lower procedence
        
        '''
        
        for operators in self.operator_procedence:
            
            if list(operators).__contains__(operator1) and list(operators).__contains__(operator2):
                return 0
            
            if list(operators).__contains__(operator1) and not list(operators).__contains__(operator2):
                return 1
            
            if not list(operators).__contains__(operator1) and list(operators).__contains__(operator2):
                return -1
            
    def is_operator(self,item):
        
        for operators in self.operator_procedence:
            
            if list(operators).__contains__(item): return True
        
        return False
    
    pointer=['$']
    reduce_operator=False
    
    @property
    def _shift_reduce(self , pivot):
    
        '''
        return True if shift
        return False if reduce
        return reduce if not an operator (False)
        
        '''
    
        if self.is_operator(pivot):
            
            result = self.compare_procedence(pivot,self.pointer[-1])

            if result == 0 or result == 1 :
                self.pointer.append(pivot)
                self.reduce_operator = False                
            else:
                self.reduce_operator =True
        
        else: self.reduce_operator = False

    def make_production(self,gramar,stack):
        
        '''
        make a production posible
        
        '''
        
        for production in gramar:
            
            if len(production) < len(stack):
                
                sub_stack = stack[ (len(stack) - len(production)):]

                
                
            
            pass
        
        pass
    
    def posible_reduction(self,stack):
        
        reductions = []
        for syntaxis in self._grammar:
            
            reduction = self.make_production(syntaxis)        
            reductions.append(reduction)
        
        return reductions
    
    
    def Shift_AST(self):
        pass
    
    def Reduce_AST(self):
        
        
        pass