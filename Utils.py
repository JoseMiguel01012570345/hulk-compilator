def isNumeric(text):
    
    if text.isnumeric():
        return True
    
    if not text.startswith('e') and text.count('e+') == 1 and text.count('+') == 1 and text.count('e') == 1 and not text.endswith('+'):
        parts = text.split('e+')
        if parts[0].isnumeric() and parts[1].isnumeric():
            return True
        return False
    
    if not text.startswith('e') and text.count('e-') == 1 and text.count('-') == 1 and text.count('e') == 1 and not text.endswith('-'):
        parts = text.split('e-')
        if parts[0].isnumeric() and parts[1].isnumeric():
            return True
        return False
    
    return False
        