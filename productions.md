
`NOTES:`

    P is an in-Line caLL , P '' is expression part caLL and P ' is an about to build function call , that derives in P or P '' , L ' is literal , S ' is string , N ' is number , B ' is boolean , V ' is vector


## Functions caLL s:

* `P '` -> L ' ( L ' , $|$ P ' L ' ,
* `P '` -> L ' ( N ' , $|$ P ' N ' ,
* `P '` -> L ' ( B ' , $|$ P ' B ' ,
* `P '` -> L ' ( P '' , $|$ P ' P '' ,
* `P '` -> L ' ( V  ' $|$ P ' V ' ,
* `P '` -> L ' ( F $|$ P ' F ,
* `P '` -> L ' ( C ' $|$ P ' C ' ,
* `P '` -> L ' ( S ' $|$ P ' S ' ,
* `P ''` -> P ' )
* `P ''` -> ( P '' )
* `P` -> P '' ;

## Strings

By default every non-token element is taken to `S '` if it is a word like inside quotation marks , `""`

* `S '` -> L '' @ L '' $|$ L ' @ L ' 
* `S '` -> L '' @@ L '' $|$ L ' @@ L ' 
* `S '` -> S ' @ S '
* `S '` -> S ' @@ S ' 
* `S '` -> N ' @ S ' 
* `S '` -> N ' @@ N ' 
* `S '` -> L '' @ S ' $|$ L ' @ S '
* `S '` -> L '' @@ S ' $|$ L ' @@ S '
* `S '` -> S ' @@ L '' $|$ S ' @@ L '
* `S '` -> L '' @ N '  $|$ L ' @ N '
* `S '` -> N ' @ L ''  $|$ N ' @ L '
* `S '` -> L '' @@ N '  $|$ L ' @@ N '
* `S '` -> N ' @@ L '' $|$ N ' @@ L '
* `S '` -> P '' @ N '  
* `S '` -> N ' @ P ''  
* `S '` -> P '' @@ N ' 
* `S '` -> N ' @@ P '' 
* `S '` -> P '' @ S '  
* `S '` -> S ' @ P ''  
* `S '` -> P '' @@ S ' 
* `S '` -> S ' @@ P '' 
* `S '` -> ( S ' )
* `S` -> S ' ;


## Expression

* E -> E ' ;


## Literals:

By default every non-token element is taken to `L ''` if it is a word like

* `D '` -> ( D ' )
* `D '` -> let E0
* `E1` -> L '' := E '
* `E0` -> L '' = E '
* `D` -> D ';
* `L '` -> ( L '' ) 

## Booleans

K -> B ' $|$ L '' $|$ P ''

* `B '` -> B ' & B ' $|$ B ' & L '' $|$ B ' & L ' $|$ L '' & B ' $|$ L ' & B ' $|$ L '' & L '' $|$ L ' & L ' $|$ L '' & P '' $|$ L ' & P '' $|$ P '' & L '' $|$ P '' & L ' $|$ P '' & B ' $|$ B ' & P '' $|$ P '' & P ''

* `B '` -> B ' or B ' $|$ B ' or L '' $|$ B ' or L ' $|$ L '' or B ' $|$ L ' or B ' $|$ L '' or L '' $|$ L ' or L ' $|$ L '' or P '' $|$ L ' or P '' $|$ P '' or L '' $|$ P '' or L ' $|$ P '' or B ' $|$ B ' or P '' $|$ P '' or P ''

* `B '` -> E ' != E ' 

* `B '` ->  N ' > N ' $|$ N ' < N ' $|$ N ' >= N ' $|$ N ' <= N ' $|$ N ' > N ' $|$ N ' < N ' $|$ N ' >= N ' $|$ N ' <= P '' $|$ P '' <= N ' $|$ P '' >= N ' $|$ N ' >= P '' $|$ N ' > P '' $|$ P '' > N ' $|$ N ' < P '' $|$ P '' < N ' $|$ N ' <= L '' $|$ N ' <= L ' $|$ L '' <= N ' $|$ L ' <= N ' $|$ L '' >= N ' $|$ L ' >= N ' $|$ N ' >= L '' $|$ N ' >= L ' $|$ N ' > L '' $|$ N ' > L ' $|$ L '' > N ' $|$ L ' > N ' $|$ N ' < L '' $|$ N ' < L ' $|$ L '' < N ' $|$ L ' < N '

*  `B '` -> E ' == E ' 

* `B '` -> ( B ' )

* E ' -> B '

## Numbers:

By default every non-token element is taken to `N '` if it is a number like

* `N '` -> N ' + N ' $|$  P '' + N ' $|$  N ' + P '' $|$  L '' + N ' $|$  L ' + N ' $|$  N ' + L '' $|$  N ' + L ' $|$  P '' + L '' $|$  P '' + L '' $|$  L '' + P '' $|$  L ' + P '' $|$  L '' + L '' $|$  L ' + L ' $|$  P '' + P ''

* `N '` -> N ' - N ' $|$  P '' - N ' $|$  N ' - P '' $|$  L '' - N ' $|$  L ' - N ' $|$  N ' - L '' $|$  N ' - L ' $|$  P '' - L '' $|$  P '' - L ' $|$  L '' - P '' $|$  L ' - P '' $|$  L '' - L '' $|$  L ' - L ' $|$  P '' - P ''

* `N '` -> N ' * N ' $|$  P '' * N ' $|$  N ' * P '' $|$  L '' * N ' $|$  L ' * N ' $|$  N ' * L '' $|$  N ' * L ' $|$  P '' * L '' $|$  P '' * L ' $|$  L '' * P '' $|$  L ' * P '' $|$  L '' * L '' $|$  L ' * L ' $|$  P '' * P ''

* `N '` -> N ' / N ' $|$  P '' / N ' $|$  N ' / P '' $|$  L '' / N ' $|$  L ' / N ' $|$  N ' / L '' $|$  N ' / L ' $|$  P '' / L '' $|$  P '' / L ' $|$  L '' / P '' $|$  L ' / P '' $|$  L '' / L '' $|$  L ' / L ' $|$  P '' / P ''

* `N '` -> N ' ^ N ' $|$  P '' ^ N ' $|$  N ' ^ P '' $|$  L '' ^ N ' $|$  L ' ^ N ' $|$  N ' ^ L '' $|$  N ' ^ L ' $|$  P '' ^ L '' $|$  P '' ^ L ' $|$  L '' ^ P '' $|$  L ' ^ P '' $|$  L '' ^ L '' $|$  L ' ^ L ' $|$  P '' ^ P ''

* `N '` -> N ' % N ' $|$  P '' % N ' $|$  N ' % P '' $|$  L '' % N ' $|$  L ' % N ' $|$  N ' % L '' $|$  N ' % L ' $|$  P '' % L '' $|$  P '' % L ' $|$  L '' % P '' $|$  L ' % P '' $|$  L '' % L '' $|$  L ' % L '  $|$  P '' % P ''

* `N '` -> N ' --  $|$ P '' -- $|$ L '' -- $|$ L ' --

* `N '` -> N ' ++ $|$ P '' ++ $|$ L '' ++ $|$ $|$ L ' ++

* `N '` -> PI

* `N '` -> e 

* `N '` -> ( N ' )

* `N` -> N ' ; 

* `N` -> L ' -= N '

* `N` -> L ' -= P ''

* `N` -> L ' -= L '

* `N` -> L ' += N '

* `N` -> L ' += P ''

* `N` -> L ' += L '

* `N` -> L ' /= N '

* `N` -> L ' /= P ''

* `N` -> L ' /= L '

* `N` -> L ' *= N '

* `N` -> L ' *= P ''

* `N` -> L ' *= L '

E ' -> N '


# in

E -> D in E

## for

E -> for( L '' in E )

##  Conditional
