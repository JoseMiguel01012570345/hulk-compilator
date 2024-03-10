class IOperatorToken:

    @property
    def Operator(self):
        """
        Operator() -> Operator
        devuelve el operador que representa
        """

        raise NotImplementedError()

    @property
    def OperatorType(self):
        """
        OperatorType() -> OperatorType
        devuelve el tipo de operador que representa
        """

        raise NotImplementedError()
    
    @property
    def Resolver(self):
        """
        devuelve la funcion encargada de resolver este operador
        """
        
        raise NotImplementedError()

    pass

class ISimbolToken:
    
    @property
    def Simbol(self):
        """
        Simbol() -> Simbol
        devuelve el simbolo que representa
        """

        raise NotImplementedError()

    @property
    def SimbolType(self):
        """
        SimbolType() -> SimbolType
        devuelve tipo de simbolo que representa
        """

        raise NotImplementedError()

    pass

class IKeywordToken:

    @property
    def Keyword(self):
        """
        Keyword() -> Keyword
        devuelve la palabra reservada que representa
        """

        raise NotImplementedError()

    @property
    def KeywordType(self):
        """
        KeywordType() -> KeywordType
        devuelve el tipo de palabra reservada que representa
        """

        raise NotImplementedError()

    pass

class ILiteralToken:

    @property
    def SelfType(self):
        """
        SelfType() -> Type
        devuelve el tipo del token que representa
        """
        raise NotImplementedError()

    pass

class IVariableToken:

    @property
    def Name(self):
        """
        Name() -> string
        devuelve el nombre de la variable que representa
        """

        raise NotImplementedError()

    pass