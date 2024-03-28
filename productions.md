
`NOTES:`

    P is an in-Line caLL , P '' is expression part caLL and P ' is an about to build function call , that derives in P or P '' , L ' is variable in brackets ( L '' ) where L '' is the variable , S ' is string , N ' is number , B ' is boolean , V ' is vector , Z '' is a L '' but before a function

## Function caLL:
 
* `P '` -> Z '' ( E ' , $|$ P ' E ' , 
* `P '` -> Z '' ( L ''' , $|$ P ' L ''' , 
* `P '` -> Z '' ( F  $|$ P ' F , 
* `P ''` -> P ' ) $|$ Z ''( E ') $|$ Z ''( F ) $|$ $|$ Z ''( L ''') $|$ P ' E ' )  $|$ P ' L ''' )  $|$ P ' F ' )
* `P ''` -> ( P '' )

## Strings

By default every non-token element is taken to `S '` if it is a word like inside quotation marks , `""`

* `G1 '` -> L '' $|$ N ' $|$ P '' $|$ S ' $|$ T '
* `S '` -> G1 ' @ G1 ' 
* `S '` -> G1 ' @@ G1 ' 
* `S '` -> ( S ' )
* `S` -> S ' ;

## Expression block

* `E '` -> S ' $|$ N ' $|$ P '' $|$ B ' $|$ L '' $|$ V ' $|$ D ' $|$ X ' $|$ T ' $|$ K $|$ G ' $|$ G1 ' $|$ W '
* `bl '` -> { }
* `bl ''` -> { E $|$ { bl ' $|$ { bl $|$ {F $|$ {C   
* `bl ''` -> bl '' E $|$ bl '' bl $|$ bl '' F $|$ bl '' C    
* `bl '` -> bl '' }
* `bl` -> bl ';
* `E '` -> ( E ' )
* `E`  -> E ';
* `T '` -> E '.P '' $|$ S '.P '' $|$ N '.P '' $|$ P ''.P '' $|$ B '.P '' $|$ L ''.P '' $|$ V '.P '' $|$ D '.P '' $|$ X '.P '' $|$ T '.P '' $|$ K.P '' $|$ G '.P '' $|$ G1 '.P '' $|$ W '.P ''
* `T '` ->  E '.L '' $|$ S '.L '' $|$ N '.L '' $|$ L ''.L '' $|$ B '.L '' $|$ L ''.L '' $|$ V '.L '' $|$ D '.L '' $|$ X '.L '' $|$ T '.L '' $|$ K.L '' $|$ G '.L '' $|$ G1 '.L '' $|$ W '.L ''

## Literals:

By default every non-token element is taken to `L ''` if it is a word like

* `D '` -> let E0
* `D ''` -> E ' , E0 $|$ E ' , E '
* `D ''` -> D '' , E0 $|$ D '' , E '
* `E '` -> L '' := E ' $|$ L ''' := E ' $|$ D ' := E '
* `E0` -> L '' = E ' $|$ L ''' = E '
* `D` -> D '; 
* `L '''` -> L '' : L '' // let x: Number = 42;
* `L ''` -> (L '')
* `L ''` ->  L '' as L ''

## Booleans

* `K` -> L '' $|$ P '' $|$ X ' $|$ T '
* `G '` -> L '' $|$ N ' $|$ P '' $|$ X ' $|$ T '
* `B '` -> K & K $|$ K $ B ' $|$ B ' $ K
* `B '` -> K | K $|$ K | B ' $|$ B ' | K
* `B '` -> E ' != E ' 
* `B '` ->  G ' > G ' $|$ G ' < G '
* `B '` ->  G ' >= G ' $|$ G ' <= G '
* `B '` -> E ' == E ' 
* `B '` ->  E ' is L ''
* `B '` -> ( B ' )
* `B` -> B ' ; 

## Numbers:

By default every non-token element is taken to `N '` if it is a number like.

* `G '` -> L '' $|$ N ' $|$ P '' $|$ X ' $|$ T '
* `G '` -> PI
* `G '` -> e 

### Operators

* `G '` -> G ' +  G '
* `G '` -> G ' -  G '
* `G '` -> G ' *  G '
* `G '` -> G ' /  G '
* `G '` -> G ' ^  G '
* `G '` -> G ' %  G '
* `G '` -> ( G ' )

### No operator , but numbers

* `N '` -> G '
* `N '` -> L '' -= G '
* `N '` -> L '' += G '
* `N '` -> L '' /= G '
* `N '` -> L '' *= G '
* `N '` -> G ' --
* `N '` -> G ' ++
* `N '` -> G '
* `N` -> G ' ; 

## in

* `E '` -> E ' in E ' $|$ D '' in E '
* `E` -> D '' in bl '
* `E` -> E ' in bl 
* `E` ->  E ' in E $|$ D '' in E 

## for

* `for` -> for( L '' in E ' ) bl '
* `for '` -> for( L '' in E ' ) E '
* `for` -> for( L '' in E ' ) bl
* `for` -> for( L '' in E ' ) E
* `E` -> for
* `E '` -> for '

##  Conditional

* `K` -> L '' $|$ P '' $|$ X ' $|$ T '
* `I` -> if ( K ) E ' $|$ if ( B ' ) E '
* `I` -> if ( K ) bl '
* `If` -> I else bl $|$ I else E $|$ if ( B ' ) E $|$ if ( K ) E 
* `I` -> I elif ( K ) bl $|$ I  elif ( K ) E ' $|$ I elif ( B ' ) bl $|$ I  elif ( B ' ) E '
* `E '` -> I else E '
* `E` -> If

## while

* `K` -> L '' $|$ P '' $|$ X ' $|$ T '
* `W`-> while( K ) E $|$ while( B ' ) E
* `W`-> while( K ) bl $|$ while( B ' ) bl
* `W` -> while( K ) bl ' $|$ while( B ' ) bl '
* `W '` -> while( K ) E ' $|$ while( B ' ) E '
* `E` -> W
  
## function

* `F` -> function P '' bl $|$ function P '' : L '' bl
* `F` -> function P '' => E $|$ function P '' : L '' => E
* `F` -> function P '' => bl $|$ $|$ function P '' : L '' => bl  
* `F` -> function P '' bl ' $|$ function P '' : L '' bl '
* `F` -> function P '' => E $|$ function P '' : L '' => E
* `F` -> function P '' => bl ' $|$ $|$ function P '' : L '' => bl ' 
  
## Types

* `C`-> type L '' bl '
* `C`-> type P '' bl ' 
* `C`-> type L '' inherits L '' bl '
* `C`-> type P '' inherits L '' bl '
* `C`-> type L '' inherits P '' bl '
* `C`-> type P '' inherits P '' bl '
* `E '` -> new P ''

## Special block

* `bls '` -> { P '' : L ''; $|$ bls ' P '' : L '';
* `bls ` -> bl 's }

## Protocols

* `Q` -> protocol L '' bls $|$ protocol L '' extends L '' bls

## Vector

* `V '` -> [ E ' || E ' in E ' ]
* `V ''` -> [ E ' , $|$ V '' E ' ,
* `V '` -> V '' ]
* `X '`-> L ''[ E ']

# Procedencia

 * Arithmetic Operations
 * Comparison Operations
 * Logical Operations
 * Assignment Operations
 * Control Flow Operations
 * Function Calls
 * Array and List Operations
 * String Operations
 * Object and Class Operations
 * Accessing properties (object.property)
 * Type Conversion


# Strategy

    Shift: ++ , --
    Shift: -+
    Reduce: -+


# Reduction Strategy

- Para saber que reduccion hacer en caso de que se tengas varias posibles, miramos los operadores a ambas partes ( izquierda y derecha ) , y nos quedamos con la produccion del operador con mas procedencia

    ej : let x := y + 4;

    let L '' := L '' + N ';

    para el segundo L '' nos quedamos con G ' y resolvemos

    let L '' := G ' + G ';

- Una vez resuelto el ultimo pivote, se pasa para el pivote anterior y se intenta parsear desde la posicion del nuevo pivote hasta el final de la cadena

### Produccion segun operador

- G ' <= ([ P '' , N ' , L '' , X ' , T ' ] , [ '+' , '-' , '*' , '/' , '^' , '%'  , '++' , '--' , '/=' , ' *= ' , '-=' , '>' , '<' , '>=' , '<=' , '!=' ] )

- G1 ' <= ([L '', N ' , P '' , S ' , T '], [ '@' , '@@' ])

- K <= ([L '' , P '' , X ' , T '],[ '&' , '|' , ')' ])

- E ' <= ([S '~ , N '~ , P ''~ , B '~ , L ''~ , V '~ , D '~ , X '~ , T '~ , K~ , G '~ , G1 '~ , W '~] , [ '.' , ',' , ';' , 'else' , 'elif' , 'in' ,' , ':=', '$' , '||' , '==' , '~' , ']' ])

- E ' <= ([ # S ' ,# N ' ,# P '' ,# B ' ,# L '' ,# V ' ,# D ' ,# X ' ,# T ' ,# K ,# G ' ,# G1 ' ,# W ' ] , [ '#' ])