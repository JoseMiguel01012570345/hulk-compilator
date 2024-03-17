
`NOTES:`

    P is an in-Line caLL , P '' is expression part caLL and P ' is an about to build function call , that derives in P or P '' , L ' is literal , S ' is string , N ' is number , B ' is boolean , V ' is vector


## Function caLL:
 
* `P '` -> L '' ( E ' , $|$ P ' E ' ,
* `P '` -> L '' ( L ''' , $|$ P ' L ''' ,
* `P '` -> L '' ( F  $|$ P ' F ,
* `P '` -> L '' ( C  $|$ P ' C  ,
* `P ''` -> P ' )
* `P ''` -> P '' 
* `P ''` -> ( P '' )
* `P` -> P '' ;

## Strings

By default every non-token element is taken to `S '` if it is a word like inside quotation marks , `""`

* `G` -> L '' $|$ L ' $|$ N ' $|$ P ''

* `S '` -> G @ G 
* `S '` -> G @@ G 
* `S '` -> S ' @ S '
* `S '` -> S ' @@ S ' 
* `S '` -> G @ S ' $|$ S ' @ G
* `S '` -> ( S ' )
* `S` -> S ' ;

## Expression block

* `E '` -> S ' $|$ N ' $|$ P '' $|$ B ' $|$ L ' $|$ L '' $|$ V $|$ D '
  
* `bl '` -> { }
  
* `bl ''` -> { E $|$ { bl ' $|$ { bl $|$ {F $|$ {C 
  
* `bl ''` -> bl '' E $|$ bl '' bl $|$ bl '' F $|$ bl '' C  
  
* `bl '` -> bl '' }

* `bl` -> bl ';

* E ' -> ( E ' )
  
* E  -> E ;

## Literals:

By default every non-token element is taken to `L ''` if it is a word like

* `D '` -> ( D ' )
* `D '` -> let E0
* `E '` -> L '' := E ' $|$ L ''' := E ' $|$ L ''' := E '
* `E0` -> L '' = E ' $|$ L ''' = E '
* `D` -> D '; 
* `L '` -> ( L '' ) 
* `L '''` -> L '' : L '' // let x: Number = 42;
* `E '` -> L ''

## Booleans

* `K` -> B ' $|$ L '' $|$ P '' $|$ L '
* `G` -> L '' $|$ L ' $|$ N ' $|$ P ''
* `B '` -> K & K
* `B '` -> K or K
* `B '` -> E ' != E ' 
* `B '` ->  G > G $|$ G < G
* `B '` ->  G >= G $|$ G <= G
*  `B '` -> E ' == E ' 
* `B '` -> ( B ' )
* `B` -> B ' ; 

## Numbers:

By default every non-token element is taken to `N '` if it is a number like

* `G` -> L '' $|$ L ' $|$ N ' $|$ P ''
* `N '` -> G + G
* `N '` -> G - G
* `N '` -> G * G
* `N '` -> G / G
* `N '` -> G ^ G
* `N '` -> G % G
* `N '` -> G --
* `N '` -> G ++
* `N '` -> PI
* `N '` -> e 
* `N` -> L ' -= G '
* `N` -> L ' += G '
* `N` -> L ' /= G '
* `N` -> L ' *= G '
* `N '` -> ( N ' )
* `N` -> N ' ; 
   
## in

* `E '` -> D ' in E ' $|$ D in bl ' 
* `E` -> D ' in bl $|$ D ' in E

## for

* E ' -> for( L '' in E ' ) bl '
* E -> for( L '' in E ' ) bl
* E -> for( L '' in E ' ) E

##  Conditional

* `K` -> B ' $|$ L '' $|$ P '' $|$ L '
* `I` -> if ( K ) E
* `I` -> if ( K ) bl
* `If` -> I else bl $|$ I else E
* `I` -> I elif ( K ) bl $|$ I  elif ( K ) E
* `E` -> If

## while

* `K` -> B ' $|$ L '' $|$ P '' $|$ L '
* `W`-> while( K ) E
* `W`-> while( K ) bl
* `W '` -> while( K ) bl '

## function

* F -> function P '' bl $|$ function P '' : L '' bl
* F -> function P '' => E $|$ function P '' : L '' => E
* F -> function P '' => bl $|$ $|$ function P '' : L '' => bl // case : function tan(x: Number): Number => sin(x) / cos(x);
  
## Types

* `C`-> type L '' bl '
* `C`-> type P '' bl ' 
* `C`-> type L '' inherits L '' bl '
* `C`-> type P '' inherits L '' bl '
* `C`-> type L '' inherits P '' bl '
* `C`-> type P '' inherits P '' bl '
* `E '` -> new P ''



