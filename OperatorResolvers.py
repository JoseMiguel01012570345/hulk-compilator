def PlusOperatorResolver(a,b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a + b
        pass
    raise Exception(f'Los valores de {a} y de {b} deben ser valores numericos')


def PPlusOperatorResolver(a):
    if type(a) == int or type(a) == float: return a + 1
    raise Exception(f'El valor de {a} debe ser un valor numerico')

def MinusOperatorResolver(a,b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a - b
        pass
    raise Exception(f'Los valores de {a} y de {b} deben ser valores numericos')


def MMinusOperatorResolver(a):
    if type(a) == int or type(a) == float: return a - 1
    raise Exception(f'El valor de {a} debe ser un valor numerico')

def MulOperatorResolver(a,b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a * b
        pass
    raise Exception(f'Los valores de {a} y de {b} deben ser valores numericos')


def DivOperatorResolver(a,b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a / b
        pass
    raise Exception(f'Los valores de {a} y de {b} deben ser valores numericos')


def ExpOperatorResolver(a,b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a ** b
        pass
    raise Exception(f'Los valores de {a} y de {b} deben ser valores numericos')

def RestOperatorResolver(a,b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a % b
        pass
    raise Exception(f'Los valores de {a} y de {b} deben ser valores numericos')

def LessThanOperatorResolver(a,b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a < b
        pass
    raise Exception(f'Los valores de {a} y de {b} deben ser valores numericos')

def GreatherThanOperatorResolver(a,b):
    return a > b

def EqOperatorResolver(a,b):
    return b

def DoubleEqOperatorResolver(a,b):
    return a == b

def DoublePointEqOperatorResolver(a,b):
    a = b
    return b

def LessEqThanOperatorResolver(a,b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a <= b
        pass
    raise Exception(f'Los valores de {a} y de {b} deben ser valores numericos')

def GreatherEqThanOperatorResolver(a,b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a >= b
        pass
    raise Exception(f'Los valores de {a} y de {b} deben ser valores numericos')

def DistintOperatorResolver(a,b):
    return not a == b

def AndOperatorResolver(a,b):
    if type(a) == type(b) == bool: return a and b
    raise Exception(f'Los valores de {a} y de {b} deben ser valores booleanos')

def OrOperatorResolver(a,b):
    if type(a) == type(b) == bool: return a or b
    raise Exception(f'Los valores de {a} y de {b} deben ser valores booleanos')

def NotOperatorResolver(a):
    if not type(a) == bool:
        raise Exception(f'{a} debe ser un valor booleano')
    return not a

def AskOperatorResolver(boolean,a,b):
    """
    Si se cumple la condicion \'boolean\' se retorna a, en otro caso se retorna b
    """
    if not type(boolean) == bool: raise Exception(f'{boolean} debe ser un valor booleano')
    if boolean: return a
    return b

def ConcatOperatorResolver(a,b):
    return str(a) + ' ' + str(b)

def IsOperatorResolver(a,b):
    return a is b

def AsOperatorResolver(a,b):
    a_list = dir(a)
    b_list = dir(b)
    
    a_is_b = True
    b_is_a = True
    error = ''
    counter = 0
    
    for value in a_list:
        if b_list.count(value) == 0:
            a_is_b = False
            break
        counter += 1
        pass

    if not a_is_b:
        error += f'La propiedad {a_list[counter]} no se encuentra en el tipo {b}.'
        pass

        counter = 0

    for value in b_list:
        if a_list.count(value) == 0:
            b_is_a = False
            break
        counter += 1
        pass
    
    if not b_is_a:
        error += f'La propiedad {b_list[counter]} no se encuentra en el tipo {a}.'
    
    
    if a_list == b_list: return a
    raise Exception(f'No se puede castear el objeto {a} al tipo {b}. {error}')