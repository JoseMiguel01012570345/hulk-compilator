
`NOTES:`

    P is an in-Line caLL , P '' is expression part caLL and P ' is an about to build function call , that derives in P or P '' , L ' is variable in brackets ( L '' ) where L '' is the variable , S ' is string , N ' is number , B ' is boolean , V ' is vector , Z '' is a L '' but before a function

## Function caLL:
 
* `P '` -> Z '' ( E ' , $|$ P ' E ' ,
* `P '` -> Z '' ( L ''' , $|$ P ' L ''' ,
* `P '` -> Z '' ( F  $|$ P ' F ,
* `P '` -> Z '' ( C  $|$ P ' C  ,
* `P ''` -> P ' )
* `P ''` -> P '' 
* `P ''` -> ( P '' )
* `P` -> P '' ;
  
## Strings

By default every non-token element is taken to `S '` if it is a word like inside quotation marks , `""`

* `G1 '` -> L '' $|$ L ' $|$ N ' $|$ P '' $|$ S ' $|$ T '
* `S '` -> G1 ' @ G1 ' 
* `S '` -> G1 ' @@ G1 ' 
* `S '` -> ( S ' )
* `S` -> S ' ;

## Expression block

* `E '` -> S ' $|$ N ' $|$ P '' $|$ B ' $|$ L ' $|$ L '' $|$ V ' $|$ D ' $|$ X ' $|$ T ' $|$ K $|$ G ' $|$ G1 '
* `bl '` -> { }
* `bl ''` -> { E $|$ { bl ' $|$ { bl $|$ {F $|$ {C   
* `bl ''` -> bl '' E $|$ bl '' bl $|$ bl '' F $|$ bl '' C    
* `bl '` -> bl '' }
* `bl` -> bl ';
* `E '` -> ( E ' )
* `E`  -> E ';
* `T '` -> E '.P '
* `T '` -> E '.L ''

## Literals:

By default every non-token element is taken to `L ''` if it is a word like

* `D '` -> ( D ' )
* `D '` -> let E0
* `D ''` -> D ' , E0
* `D ''` -> D '' , E0
* `D` -> D '' ;
* `E '` -> L '' := E ' $|$ L ''' := E ' $|$ L ''' := E '
* `E0` -> L '' = E ' $|$ L ''' = E '
* `D` -> D '; 
* `L '` -> ( L '' ) 
* `L '''` -> L '' : L '' // let x: Number = 42;
* `E '` -> L ''

## Booleans

* `K` -> L '' $|$ P '' $|$ L ' $|$ X ' $|$ T '
* `G '` -> L '' $|$ L ' $|$ N ' $|$ P '' $|$ X ' $|$ T '
* `B '` -> K & K $|$ K $ B ' $|$ B ' $ K
* `B '` -> K || K
* `B '` -> E ' != E ' 
* `B '` ->  G ' > G ' $|$ G ' < G '
* `B '` ->  G ' >= G ' $|$ G ' <= G '
* `B '` -> E ' == E ' 
* `B '` ->  E ' is E '
* `B '` -> ( B ' )
* `B` -> B ' ; 

## Numbers:

By default every non-token element is taken to `N '` if it is a number like.

* `G '` -> L '' $|$ L ' $|$ N ' $|$ P '' $|$ X ' $|$ T '
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
* `N '` -> L ' -= G '
* `N '` -> L ' += G '
* `N '` -> L ' /= G '
* `N '` -> L ' *= G '
* `N '` -> G ' --
* `N '` -> G ' ++
* `N '` -> G '
* `N` -> G ' ; 

## in

* `E '` -> D ' in E ' $|$ D ' in bl ' 
* `E '` -> D '' in E ' $|$ D '' in bl ' 
* `E` -> D ' in bl $|$ D ' in E
* `E` -> D '' in bl $|$ D '' in E

## for

* `for '` -> for( L '' in E ' ) bl '
* `for` -> for( L '' in E ' ) bl
* `for` -> for( L '' in E ' ) E

##  Conditional

* `K` -> B ' $|$ L '' $|$ P '' $|$ L ' $|$ X ' $|$ T '
* `I` -> if ( K ) E
* `I` -> if ( K ) bl
* `If` -> I else bl $|$ I else E
* `I` -> I elif ( K ) bl $|$ I  elif ( K ) E
* `E` -> If

## while

* `K` -> B ' $|$ L '' $|$ P '' $|$ L ' $|$ X ' $|$ T '
* `W`-> while( K ) E
* `W`-> while( K ) bl
* `W '` -> while( K ) bl '

## function

* `F` -> function P '' bl $|$ function P '' : L '' bl
* `F` -> function P '' => E $|$ function P '' : L '' => E
* `F` -> function P '' => bl $|$ $|$ function P '' : L '' => bl  // case : function tan(x: Number): Number => sin(x) / cos(x);
  
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

* `V '` -> [ E ' || L '' in E ' ]
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

n + n * * n * n ^ n ^ n - n * n ^ n

