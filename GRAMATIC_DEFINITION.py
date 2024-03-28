import HULK_LANGUAGE_DEFINITION as HK

function_caLL={
    "P '"  : ["L ''(E ',","P 'E ' ","L ''(L '''","P 'L '''" ,"L ''(F," ,"P 'F" , "L ''(C","P 'C"  ,],
    "P ''" : ["(P '')"],
    "P"    : ["P '';"],
}
strings={
    "S '": ["E '@E ' ","E '@@E ' ","(S ')"],
    "S"  :[ "S ';"],
}
expression_block = {
    
    "E '" : ["S '","N '", "P ''" , "B '","L '", "L ''","V '", "D '" ,"X '","(E ')" ],
    "bl '":[ "{ }", "bl ''}"],
    "bl ''": ["{E", "{bl '" ,"{bl" ,"{F", "{C", "bl ''E" , "bl ''bl", "bl ''F","bl ''C"],
    "bl" : ["bl ';",],
    "E" : ["E;"],
}
literals={
    
"D '" : [ "(D ')" , "letE0" , "L ''" ],
"E '" : [ "L '':=E '" , "L ''' := E '" , "L ''':=E '" ],
"E0" : [ "L ''=E '",  "L '''=E '" ],
"D" : [ "D ';" ],
"L '" : [ "(L '')" ],
"L '''" : [ "L '':L ''" ],
   
}

booleans = {
    
    "K" : ["B '" , "L ''" , "P ''" , "L '" , "X '"],
    "G '" : ["L ''" , "L '" , "N '" , "P ''" , "X '"],
    "B '" : ["K&K" , "K||K" , "E '!=E '", "G '>G '" , "G '<G '" , "G '<=G '" , "G '>=G '" , "E '==E '" , "E 'isE '" , "(B ')" ,"B ';" ],

}

numbers = {
    
    "G '" : ["L ''" , "L '" , "N '" , "P ''" ,  "X '" , "PI" , "e" ,"G '+G '", "G '-G '", "G '*G '", "G '/G '", "G '^G '", "G '%G '", "(G ')"],
    "N '" : [ "L '-=G '" ,"L '+=G '" ,"L '/=G '" ,"L '*=G '" , "G '--" , "G '++" , "G '" , "G ';" ]
}

IN = {
    "E '": ["D 'inE '",  "D 'inbl '", "D 'inbl" , "D 'inE"]
}
FOR = {
    
    "E '" : [ "for(L ''inE ')bl '" ],
    "E" : [ "for(L ''inE ')bl" , "for(L ''inE ')E" ]
    
} 
# Conditional
# while
# function
# Types
# Special block
# Protocols
# Vector

def traslator(token_list):
    
    print(token_list)
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
        for arg in HK.SYMBOLS_and_OPERATORS_parser:            
            
            if token_list[index] == arg:
                
                if arg == 'is':
                
                    parse_list.append("~")                    
                    parse_list.append(token_list[index])
                    kw =True
                    break
                
                if arg == "==":
                    parse_list.append(token_list[index])
                    parse_list.append("#")                    
                    kw =True
                    break
                
                parse_list.append(token_list[index])
                kw =True
                break
            
        if not kw:
            if index + 1 < len(token_list) and token_list[index + 1 ] == "(" :
                parse_list.append("Z ''")
            
            else:
                parse_list.append("L ''")
        index += 1
    
    parse_list.append("$")
    return parse_list
