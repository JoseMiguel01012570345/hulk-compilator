
'''
NOTE:

token_list is of the form : ( label , ASTNode )

'''

class ASTNode:
      
    anotated_type = None
    hash_ = 0
    
    def my_self(self):
        
        if self.def_node():
            return { 'id': self.id  , 'name': self.name  }
    
    def set_identifier(self,id_:str):  
        
        self.id = id_
        
        return self.id
    
    def def_node(self):
        
        def_node = ['function_form','protocol','type','let','super_class','build_in']
        
        for item in def_node:
            
            if item == self.id:
                return True
        
        return False
    
    def send_context(self): 
        
        '''
        pass the context from one child to another
        
        '''
        
        children: list = self.visitor()
        
        if children == None : return
        
        if type(children) == list:
        
            for child in children:
                
                if child == None: continue
                
                my_context = [ item for item in self.context]
                child.context = [ item for item in my_context ]
                child.send_context()
            
                pass
        else:
            my_context = [ item for item in self.context]
            
            if children != None:
                children.context = [ item for item in my_context ]
                children.send_context()
        
        pass
    
    def context_check(self):
        
        children = self.visitor()
        
        for child in children:
            
            if type(child) == list:
                
                for element in child:
                    element.context_check()
                    
                pass
            
            else:
                child.context_check()
        
        pass
        
    def type_checking(self):
        pass        

    def visitor(self):
        
        '''
        visitor returns a list of elements you can visit
        example: 
        
            while condition 
                
                body
                
            "visitor" returns : [ condition , body ]
        
        by default "visitor" returns binary operation visitation
        
        '''
        
        return [ self.left , self.right ]
    
    def cil_node_code(self):
        """
        return CIL codes

        """
        pass

  
class AST(ASTNode):
    pass

class function_call( AST): # check context

    '''
    atributes of this class are:
    
    > id
    > name : FunctionCall
    > args
    
    '''
    
    context = []
    avaliable = False
    
    def __init__( self, token_list ):
        
        if self.validator(token_list):
        
            self.set_identifier('FunctionCall')
            self.name = token_list[0][1].name
            self.args = token_list[1][1]
            self.avaliable = True
        
        pass
    
    def visitor(self):
        
        if self.args != None and self.args.id == 'parameters':
            return self.args
    
        else: return [self.args]
    
    def context_check(self):
        
        exist = [ item for item in self.context if item.id == 'function_form' and def_function(item).name == self.name ] 
        
        if len(exist) != 0 :
            return True
        
        return False
    
    def type_checking(self):
        return super().type_checking()
    
    pass
        
    def validator(self, token_list):
        
        if token_list[0][0] == 'c': return True
    
class params( AST):
    
    '''
    atributes of this class are:
    
    > id : params
    > parameters
    
    '''
    
    parameters = []
    avaliable = False
    context = []
    
    def __init__(self,token_list):
        
        self.set_identifier('params')
        
        if self.validator(token_list): self.avaliable = True
        
        if self.avaliable and token_list[0][0] == 'p': # if the first token is a param
            
            self.parameters = [ item for item in token_list[0][1].parameters ]
            
        elif self.avaliable:
            
            param1 = token_list[0][1]
            new_parameters = []
            
            if token_list[2][0] == 'p': #  if second token is a param, unbox param "p"
                
                new_parameters = [ item for item in token_list[2][1].parameters ]
                new_parameters.insert(0,param1)
                self.parameters = new_parameters
            else:
                    
                param2 = token_list[2][1]
                new_parameters.append(param1)
                new_parameters.append(param2)
                self.parameters = new_parameters
        
    def visitor(self):
        return self.parameters
                            
    def validator(self,token_list):
        
        if token_list[0][0] == 'p': return True
        
        if len(token_list)>1 and token_list[1][0] == ',': return True
        
        return False

    pass

class binary_expression:
    
    '''
    this class selects the kind of binary expression the token_list refers to. Every
    class in this class has as attributes:
    
    > id : the kind of expression it is specified by its symbol
    > left: left member
    > right: right member
    
    '''
    
    avaliable = False
    AST_binary = None
    def __init__(self,token_list:list):
        
        if self.validator(token_list):
        
            self.avaliable = True
        
            binary_expresion =[ ('+',self.plus(token_list)) , ('-', self.minus(token_list)) ,
                                ('*', self.multiplication(token_list)) ,('/', self.divition(token_list)) ,
                                ('^', self._pow(token_list)),('**', self._pow(token_list)),
                                ('%', self.per_cent(token_list)),('@', self.concatenation(token_list)),
                                ('@@', self.blank_space_concatenation(token_list)), (':',self.double_dot(token_list)),
                                (':=', self.double_dot_equal(token_list)), ('as',self.as_(token_list)),
                                ('is', self.is_(token_list)), ('==',self.equal(token_list)),
                                ('>', self.bigger_than(token_list)), ('<',self.smaller_than(token_list)),
                                ('>=', self.bigger_or_equal(token_list)), ('<=',self.smaller_or_equal(token_list)),
                                ('=', self.assign(token_list)), ('|',self.or_(token_list)),
                                ('&', self.and_(token_list)), ('!=',self.different(token_list)),
                                ('/=', self.divide_and_assign(token_list)), ('*=',self.multiply_and_assign(token_list)),
                                ('+=', self.plus_and_assign(token_list)), ('-=',self.minus_and_assign(token_list)),
                                ('in', self.in_(token_list)) , ('.', self.dot(token_list))
                                ]
        
            for item in binary_expresion:
        
                if item[0] == token_list[1][0]:
        
                    self.AST_binary = item[1]
                    return
    
    def validator(self,token_list):
        
        operators = [ '.', '-=', '*=', '!=', '|', '<=', '<', '==', 'as', ':', '@', '**', '/',
                        '-', '+' , '*' , '^' , '%' , '@@', ':=', 'is', '>' , '>=', '=' , '&' ,
                        '/=', '+=', 'in' ]
        try:
        
            if operators.__contains__(token_list[1][0]):
                return True
        
        except: pass
        
        return False

    class dot(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('.')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
            pass
        
        pass
        
        def visitor(self):
            return [ self.left , self.right ]
    class in_(AST):
        
        context = []        
        def __init__(self,token_list):
            
            self.set_identifier('in')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
            pass
        
        def visitor(self):
            return super().visitor()
        
        def retrive_var_context(self,node:ASTNode):
        
            if node.id == 'let':
                
                return { 'id': 'let', 'name': node.left.name }
            
            return None

    def create_context(self,args_AST:list):
        
        params_context = []
        if args_AST == None : return []
        
        if type(args_AST) == list:
            for param in args_AST:
                
                var = self.retrive_var_context(param)
                if var != None:
                    params_context.append(var)
            
        else:
            arg = self.retrive_var_context(args_AST)
            params_context.append( arg )
        
        return params_context

    def send_context(self):
        
        new_context = [ item for item in self.context ]
        params_context = self.create_context(args_AST= self.left)
        
        self.left.context = self.merge_context(params_context,new_context)
        self.left.send_context()
    
        if self.right != None:
            
            body_context = self.merge_context(params_context,new_context)
            
            self.body.context = body_context
            self.body.send_context()
        
        pass
    
    def merge_context(self,contex1,contex2):
        
        result_context = [  ]
        for item in contex2:
            
            result_context.append(item)
        
        for item in contex1:
            
            if self.equal(item,result_context):
                continue
            
            result_context.append(item)
        
        return result_context
        
    def equal(self,node1,new_context):
        
        if node1 == None : return False
        for item in new_context:
        
            if node1['id'] == item['id'] and node1['name'] == item['name'] : return True
        
        return False
     
        
        pass

    class plus(AST):
            
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('+')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
        pass      
    
        def visitor(self):
            return super().visitor()    
  
    class minus(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('-')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
        def visitor(self):
            return super().visitor()
    
    class multiplication(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('*')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
        def visitor(self):
            return super().visitor()
    
    class divition(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('/')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
        def visitor(self):
            return super().visitor()
    
    class _pow(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('^')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
        def visitor(self):
            return super().visitor()
    
    class per_cent(AST):
        
        context = []        
        def __init__(self,token_list):
            
            self.set_identifier('%')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
        def visitor(self):
            return super().visitor()
    
    class concatenation(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('@')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
        
        def visitor(self):
            return super().visitor()
    class blank_space_concatenation(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('@@')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
        def visitor(self):
            return super().visitor()
   
    class double_dot(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier(':')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
        
        def visitor(self):
            return super().visitor()
    
    class double_dot_equal(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier(':=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    
    class as_(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('as')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
        pass
    
        def visitor(self):
            return super().visitor()
    class is_(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('is')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
        pass
        
        def visitor(self):
            return super().visitor()
    
    class equal(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('==')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
        
        def visitor(self):
            return super().visitor()
    class bigger_than(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('>')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    
    class smaller_than(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('<')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    
    class bigger_or_equal(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('>=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    
    class smaller_or_equal(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('<=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    
    class assign(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    class or_(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('|')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    
    class and_(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('&')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
        
        def visitor(self):
            return super().visitor()
    class different(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('!=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    
    class divide_and_assign(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('/=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    class multiply_and_assign(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('*=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    
    class plus_and_assign(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('+=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()
    
    class minus_and_assign(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('-=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
        def visitor(self):
            return super().visitor()

class unary_expression:
    
    '''
    this class selects the kind of binary expression the token_list refers to. Every
    class in this class has as attributes:
    
    > id : the kind of expression it is specified by its symbol
    > right: right unary member
    
    '''
    
    avaliable = False
    AST_unary = None
    def __init__(self,token_list):
    
        unary_operators = ['!','++','--','new','let']
        if not unary_operators.__contains__(token_list[0][0]):            
            pass
        
        else:
            self.avaliable = True
            
            unary = [ ('!',self.not_(token_list)),
                    ('++',self.plus_plus(token_list)),
                    ('--',self.minus_minus(token_list)),
                    ('new',self.new(token_list)),
                    ('let',self.let(token_list)),
                    ]
            
            for item in unary:
                
                if item[0] == token_list[0][0]:
                    
                    self.AST_unary = item[1]
                    return

    class new(AST):

        context = []
        def __init__(self,token_list):
            
            self.set_identifier('new')
            self.right = token_list[1][1]
            
            pass
        
        def context_check(self):
        
            exist = [ item for item in self.context if AST(item).id == 'type' and type_(item).name == self.name ] 
            
            if len(exist) != 0 :
                return True
            
            return False
        
        def visitor(self):
            return self.right
        
    class let(AST):
        
        context = []
        def __init__(self,token_list):
            
            if token_list[0][0] == 'let':
            
                self.set_identifier('let')
                self.right = token_list[1][1]
                
                try:
                    self.name = token_list[1][1].left.name
                except:
                    raise Exception('no inicialization for let')
            
        def visitor(self):
            return self.right

    class not_(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('!')
            self.right = token_list[1][1]
            
        def visitor(self):
            return self.right
    class plus_plus(AST):
        
        context = []    
        def __init__(self,token_list):
            
            self.set_identifier('++')
            self.right = token_list[1][1]
    
        def visitor(self):
            return self.right
    
    class minus_minus(AST):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('--')
            self.right = token_list[1][1]
            
        def visitor(self):
            return self.right
     
class variable(AST): # check context
    
    '''
    this class has the attributes:
    
    > id : var
    > name: name of the variable
    
    '''
    
    avaliable = False
    context = []
     
    def __init__(self,token_list):
        
        try:
            if not token_list[0][0].Type.name == 'Variable' and not token_list[0][0].KeywordType.name == 'Function'  :
                pass
            
            else:
                self.avaliable = True
                self.set_identifier('var')
                self.name=token_list[0][0].Text
        
        except : pass
    
    def visitor(self):
        return None

    def context_check(self):
        
        for item in self.context:
            
            if item.id == 'let' and variable(item).name == self.name :
                return True
        
        return False

class if_(AST):
    
    '''
    this class has the attributes:
    
    > id : if
    > condition : condition for if statement
    > body: body of the statement
    
    '''
    
    avaliable = False
    context = []
    def __init__(self,token_list):
        
        if token_list[0][0] == 'if': 
            
            self.avaliable = True
            self.set_identifier('if')
            
            self.condition = token_list[1][1]
            self.body = token_list[2][1]
        
        pass
    
    pass

    def visitor(self):
        return [ self.condition , self.body ]

class elif_(AST):
    
    '''
    this class has the attributes:
    
    > id : elif
    > condition : condition for elif statement and the condition for the if statement , the condition is a list
    > body: body of the statement
    
    NOTE:
    
    The condition is a list that refers to if statement , and has second element has the elif statement
    
    '''
    
    avaliable = False
    condition=None
    context = []
    
    def __init__(self,token_list):
        
        if (token_list[0][0] == 'if' and token_list[1][0] == 'elif') : 
            
            self.avaliable = True
            self.set_identifier('elif')
            
            self.condition = [ token_list[0][1] , token_list[2][1] ]
            self.body = token_list[3][1]
        
        pass
    
    def visitor(self):
        return [ self.condition , self.body  ]
        
    pass

class else_(AST):
    
    
    '''
    this class has the attributes:
    
    > id : else
    > condition : condition for else is the condition for the if statement and condition for the
                elif statement, the condition is a list that refers to elif
    > body: body of the statement
    
    
    NOTE:
    
    the condition is a list to refers to elif statement , in case it exists , or tho the if statement in worst case
    
    '''
    
    avaliable = False
    condition = None
    context = []
    
    def __init__(self,token_list):
        
        if token_list[1][0] == 'else' : 
            
            self.avaliable = True
            self.set_identifier('else')
            
            self.condition = token_list[0][1]
            
            self.body = token_list[2][1]
        
        pass
    
    pass

    def visitor(self):
        return [ self.condition , self.body ]

class def_function(AST):
    
    '''
    atributes of this class are:
    
    > id : function_form
    > name: name of the function declared
    > args
    > body
    
    '''
    
    avaliable = False
    context = []
    
    def __init__(self,token_list):
        
        self.name = None
        self.args = None
        self.body = None
        
        if self.validator(token_list):
            
            self.avaliable= True
            self.set_identifier('function_form')
            
            if token_list[0][0] == 'function': 
                self.function_kw(token_list)
                        
            elif token_list[0][1].id == 'FunctionCall': 
                self.simple_form(token_list)
        
    def retrive_var_context(self,node:ASTNode):
        
        if node != None and node.id == ':' and node.left.id == 'var' :
            
            return { 'id': 'var', 'name': node.left.name }
        
        elif node != None and node.id == 'var' :
            return { 'id': 'var', 'name': node.name }
        
        return None

    def create_context(self,args_AST:list):
        
        params_context = []
        if args_AST == None : return []
        
        if args_AST.id == 'parameters':
            for param in args_AST.parameters:
                
                var = self.retrive_var_context(param)
                if var != None:
                    params_context.append(var)
            
        else:
            arg = self.retrive_var_context(args_AST)
            params_context.append( arg )
        
        return params_context

    def send_context(self):
        
        new_context = [ item for item in self.context ]
        params_context = self.create_context(args_AST= self.args)
        my_type = self.my_self()
        
        if self.equal(my_type,new_context):
                
            raise Exception(f'\033[1;31;40m; {self.name} already exists  \033[0m;')
            
        else:    
            new_context.append(my_type)
        
        if self.args != None:
            self.args.context = self.merge_context(params_context,new_context)
            self.args.send_context()
        
        if self.body != None:
            
            body_context = self.merge_context(params_context,new_context)
            
            self.body.context = body_context
            self.body.send_context()
        
        pass
    
    def merge_context(self,contex1,contex2):
        
        result_context = [  ]
        for item in contex2:
            
            result_context.append(item)
        
        for item in contex1:
            
            if self.equal(item,result_context):
                continue
            
            result_context.append(item)
        
        return result_context
        
    def equal(self,node1,new_context):
        
        if node1 == None : return False
        for item in new_context:
        
            if node1['id'] == item['id'] and node1['name'] == item['name'] : return True
        
        return False
    
    def function_kw(self,token_list):
        
        self.name = token_list[1][1].name
        self.args = token_list[1][1].args
        
        if token_list[2][0] == 'b' or token_list[2][0] == 'E':
        
            # function f b | function f E
            self.body = token_list[2][1]
    
        
        if token_list[2][0] == '=>':
        
            # function f => E | function f => b
            self.body = token_list[3][1]
        
        elif token_list[2][0] == ':':
        
            self.anotated_type = token_list[3][1]
            
            if token_list[4][0] == '=>':
                
                # function f : T => b | function f : T => E
                self.body=token_list[5][1]
            
            else:
                # function f : T b
                self.body=token_list[5][1]
        
    def simple_form(self,token_list):
        
        self.name = token_list[0][1].name
        self.args = token_list[0][1].args
        
        if token_list[1][0] == ":":
            
            # c():T
            self.anotated_type = token_list[2][1]
            
            if len(token_list)>4:
                
                # c():T => b
                self.body = token_list[4][1]
            
            elif len(token_list) > 3:
                
                # c():T b
                self.body = token_list[3][1]
            
        elif token_list[1][0] == "=>":
            
            # c() => E | c() => b
            self.body = token_list[2][1]
        
        else:
            
            # c() E | c() b
            self.body = token_list[1][1]

    def visitor(self):
        return [ self.args , self.body ]

    def validator(self,token_list):
        
        try:
            if token_list[0][0] == 'function': return True
            
            if token_list[0][1].id == 'FunctionCall' and (token_list[1][0] == ':' or token_list[1][0] == '=>' ):
                return True
        
        except:
            pass
        
        return False
    
    pass

class type_(AST): # check context
    
    '''
    atributes of this class are:
    
    > id : type
    > name: name of the type
    > constructor: constructor params
    > parent_name: the name of the class this class inherits from
    > base: parents constructor
    > body
    
    '''
    
    avaliable = False
    context = []
    def __init__(self,token_list):
        
        if token_list[0][0] == 'type':
            
            self.set_identifier('type')
            
            self.avaliable = True
            
            self.name = token_list[1][1].name
            self.body = None
            self.constructor = None
            self.anotated_type = self.name
            
            if token_list[1][1].id == 'FunctionCall':
                self.constructor = token_list[1][1].args
            
            self.parent_name = None
            self.base = None
            
            if token_list[2][0] == 'inherits' :
                
                self.parent_name = token_list[3][1].name
                
                if token_list[3][1].id == 'FunctionCall':
                    self.base = token_list[3][1].args
                
                self.body = token_list[4][1]
            
                if self.constructor != None and self.base != None:
                    self.avaliable = True
                    
            else:
                self.body = token_list[2][1]
        pass
    
    def context_check(self):
        
        if self.parent_name != None:
            for item in self.context:
                
                if item.id == 'type' and item.parent_name == self.parent_name: 
                    return True
        
            return False
        
        else: return True

    def retrive_var_context(self,node:ASTNode):
        
        if node != None and  node.id == ':' and node.left.id == 'var' :
            
            return { 'id': 'var', 'name': node.left.name }
        
        elif node != None and node.id == 'var' :
            return { 'id': 'var', 'name': node.name }
        
        return None

    def create_context(self,args_AST:list):
        
        params_context = []
        if args_AST == None : return []
        
        if args_AST.id == 'params':
       
            for param in args_AST.parameters:
                
                var = self.retrive_var_context(param)
                if var != None:
                    params_context.append(var)
        else: 
            arg = self.retrive_var_context(args_AST)
            params_context.append( arg )
        
        return params_context

    def send_context(self):
        
        new_context = [ item for item in self.context ]
        params_context = self.create_context(args_AST= self.constructor)
        my_type = self.my_self()
        
        if self.equal( my_type , new_context ):
                
            raise Exception(f'\033[1;31;40m; {self.name} already exists  \033[0m;')
            
        else:    
            new_context.append(my_type)
        
        if self.constructor != None:
            self.constructor.context = self.merge_context(params_context,new_context)
            self.constructor.send_context()
        
        if self.base != None:
            base_context = self.create_context(args_AST= self.base)
            self.base.context = base_context
            self.base.send_context()
        
        if self.body != None:
            body_context = self.merge_context(params_context,new_context)
            
            self.body.context = body_context
            self.body.send_context()
        
        pass
    
    def merge_context(self,contex1,contex2):
        
        result_context = [  ]
        for item in contex2:
            
            result_context.append(item)
        
        for item in contex1:
            
            if self.equal(item,result_context):
                continue
            
            result_context.append(item)
        
        return result_context
    
    def equal(self,node1,new_context):
        
        if node1 == None : return False
        for item in new_context:
        
            if node1['id'] == item['id'] and node1['name'] == item['name'] : return True
        
        
        return False
    
    def visitor(self):
        return [ self.constructor , self.base , self.base ]

class protocol(AST): # check context
    
    '''
    atributes of this class are:
    
    > id : protocol
    > name: name of the type
    > parent_name: the name of the class this class inherits from
    > body
    
    '''
    
    avaliable = False
    context = []
    
    def __init__(self,token_list):
        
        if token_list[0][0] == 'protocol':
            
            self.avaliable = True
        
            self.set_identifier('protocol')
                
            self.name = token_list[1][1].name
            self.body = None
            self.anotated_type = self.name
            
            self.parent_name = None
        
            if token_list[2][0] == 'extends' :
                
                self.parent_name = token_list[3][1].name
                self.body = token_list[4][1]
                    
            else:
                self.body = token_list[2][1]
    
        pass
    
    def context_check(self):
        
        for item in self.context:
            
            if item.id == 'protocol' and item.parent_name == self.parent_name: 
                return True
        
        return False
    
    def visitor(self):
        return [ self.body ]

class vectors(AST):
    
    '''
    
    vector forms: 
    1. [ filter || domain ]
    2. [ 1,2,3,4, ... ]
    
    attributes:
    
    > filter_ : the filter of a vector
    > domain: the domain of a vector
    
    '''
    
    avaliable = False
    filter_ = None
    domain = None
    context = []
        
    def __init__(self,token_list):
        
        self.set_identifier('vector')
        
        if self.validator(token_list):
            
            self.avaliable = True

            self.array_(token_list)
            
    def validator(self,token_list):
        
        if token_list[0][0] == '[': return True
        
        return False
    
    def array_(self,token_list):
        
        if token_list[1][0] == 'p':
            
            self.domain = [ item for item in token_list[1][1].parameters ]
            
        elif token_list[1][0] == 'T' :
            
            self.filter_ = token_list[1][1]
            self.domain = token_list[3][1]        

    def visitor(self):
        return [ self.filter_ , self.domain ]

class literal(AST):
    
    '''
    attributes:
    
    > id: literal
    > value: value of the literal
    
    '''
    
    value = None
    avaliable = False
    context = []
    
    def __init__(self,token_list):
        
        if self.validator(token_list) :
            pass
        
        else:
            self.avaliable = True
            self.set_identifier('literal')
            self.value = token_list[0][0].Text
            
    def validator(self,token_list):
        
        try:
            if token_list[0][0].SelfType == 'Number' or token_list[0][0].SelfType == 'String' or token_list[0][0].SelfType == 'Boolean':
                return True
        except:    
            return False
    
    def visitor(self):
        return None
    
    pass

class index(AST): # check context
    
    '''
    attributes:
    
    > id : index
    > name: name of the indexation vector
    > index : index of the vector 
    
    '''
    
    avaliable = False
    args = None
    name = None
    context = []
    
    def __init__(self,token_list):
        
        if self.validator(token_list):
            
            self.avaliable = True
            self.set_identifier('index')
            self.name = token_list[0][1].name
            self.index = token_list[2][1]      
        
        pass
    
    def validator(self,token_list):
        
        target = ["T","[" , "T" , "]" ]  
        try:
            index = 0
            while index < len(token_list):
                
                if token_list[index][0] != target[index]: return False
                
                index += 1
                                
        except: 
            return False
        
        return True
    
    def context_check(self):
        
        for item in self.context:
            
            if item.id == 'var' and item.name == self.name : 
                return True
        
        return False
    
    def visitor(self):
        return [self.index]
class while_(AST):
    
    '''
    attributes:
    
    > id : while
    > condition : condition of the while loop
    > body
    
    '''
    
    avaliable = False
    condition = None
    body = None
    context = []
    
    def __init__(self,token_list):
        
        if self.validator(token_list):
            
            self.avaliable = True
            self.set_identifier('while')
            self.condition = token_list[1][1]
            self.body = token_list[2][1]
        
        pass
    
    def validator(self,toke_list):
        
        if toke_list[0][0] == 'while':
            return True
        
        return False
    
    def visitor(self):
        return [ self.condition , self.body ]

class for_(AST):
    
    '''
    attributes:
    
    > id : for
    > condition : condition of the for loop
    > body
    
    '''
    
    avaliable = False
    condition = None
    body = None
    context = []
    
    def __init__(self,token_list):
        
        if self.validator(token_list):
            
            self.avaliable = True            
            self.set_identifier('for')
            self.condition = token_list[1][1]
            self.body = token_list[2][1]
        
        pass
    
    def send_context(self):
        return super().send_context()
    
    def validator(self,toke_list):
        
        if toke_list[0][0] == 'for':
            return True
        
        return False
    
    def visitor(self):
        return [ self.condition , self.body ]

class block(AST):
    
    '''
    attributes:
    
    > id : block
    > expressions : expressions inside of the block
    
    >> solve from left to right
    
    '''
    
    expressions = [] 
    avaliable = False
    context = []
    
    def __init__(self,token_list):
        
        self.expressions = []
        self.avaliable = False
        self.context = []
        self.set_identifier('block')
        
        if self.validator(token_list): 
            
            self.avaliable = True
            
            if len(token_list) == 1: # if the first token is a param
                
                if token_list[0][0] == 'M':
                    self.expressions = token_list[0][1]
                else: 
                    self.expressions = token_list[0][1].expressions

            else:
                
                if token_list[0][0] == 'O':
                    
                    self.expressions = token_list[0][1].expressions
                    
                    if type(self.expressions) == list:
                        self.expressions.append(token_list[1][1])
                    
                    else:
                        new_expression_set = [self.expressions , token_list[1][1]]
                        self.expressions = new_expression_set
                    
                    pass
                
                elif token_list[1][0] == 'O':
                    
                    self.expressions.append(token_list[0][1])
                    
                    for item in token_list[1][1].expressions:
                        self.expressions.append(item)
                    
                    pass
                else:
                    self.expressions.append(token_list[0][1])
                    self.expressions.append(token_list[1][1])
    
    def send_context(self):
        
        new_context = [ item for item in self.context ]
        
        if type(self.expressions) == list:
            
            for expression in self.expressions:
            
                # nodes that define new variables , increases context
                if expression.def_node() : 
                    
                    expression_type = expression.my_self()
                    if self.equal(expression_type,new_context):
                
                        raise Exception(f'\033[1;31;40m; {self.name} already exists  \033[0m;')

                    else:
                        expression.context = [ item for item in new_context ]
                        expression.send_context()
                        new_context.append(  expression_type )
                else:
                    expression.context = [ item for item in new_context ]
                    
        else:
                expression = self.expressions
                
                if expression.def_node() : 
                    
                    expression_type = expression.my_self()
                    if self.equal(expression_type,new_context):
                
                        raise Exception(f'\033[1;31;40m; {self.name} already exists  \033[0m;')

                    else:
                        expression.context = [ item for item in new_context ]
                        expression.send_context()
                        new_context.append(  expression_type )
                
        
        pass
    
    def equal(self,node1,new_context):
        
        if node1 == None : return False
        for item in new_context:
        
            if node1['id'] == item['id'] and node1['name'] == item['name'] : return True
        
        
        return False
    
    def validator(self,token_list):
        
        return True
    
    def visitor(self):
        return self.expressions
    