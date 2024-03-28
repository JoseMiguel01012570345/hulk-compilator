import HULK_LANGUAGE_DEFINITION as HK

# Function caLL:
# Strings
# Expression block
# Literals:
# Booleans
# Numbers:
# in
# for
# Conditional
# while
# function
# Types
# Special block
# Protocols
# Vector

def traslator(token_list):
    
    parse_list=[]
    index=0
    while index < len(token_list ):
        
        try:
            
            if token_list[index] == "PI" or token_list[index] == "e"  or float(token_list[index])  :
                parse_list.append("N '")
                index += 1
                continue
        
        except:
            pass
        
        if token_list[index] =="'" or token_list[index] == "\"" : 
            
            index1 = index + 1
            while index1 < len(token_list):
                
                if token_list[index1] == "'" or token_list[index1] == "\"" :
                    parse_list.append("S '")
                    index = index1
                    index += 1
                    break
                
                index1 +=1
                    
        kw = False                    
        for arg in HK.SYMBOLS_and_OPERATORS:            
            
            if token_list[index] == arg:
                
                parse_list.append(token_list[index])
                kw =True
                break
        if not kw:
            parse_list.append("L ''")
        
        print(parse_list)
        index += 1
            
    return parse_list