class Token:

    def __init__(self,Text):
        self._text = Text
        pass

    @property
    def Text(self):
        """
        Text() -> string
        devuelve el texto correspondiente a este token
        """
        return self._text

    @property
    def Type(self):
        """
        Type() -> TokenType
        devuelve el tipo correspondiente a este token
        """
        raise NotImplementedError()

    @property
    def Length(self):
        """
        Length() -> int
        devuelve la longitud del texto de este token
        """
        return len(self._text)

    def __str__(self):
        """
        devuelve el texto correspondiente a este token
        """
        return self._text

    pass