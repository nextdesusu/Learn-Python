#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

arg = lambda : ( len( sys.argv ) > 1 and int( sys.argv[ 1 ] ) ) or \
    int( input( "число?: " ) )

factorial = lambda x: ( ( x == 1 ) and 1 ) or x * factorial( x - 1 )

n = arg()
m = sys.getrecursionlimit()
if n >= m - 1 :
    sys.setrecursionlimit( n + 2 )
    print( "глубина рекурсии превышает установленную в системе {}, переустановлено в {}".\
          format( m, sys.getrecursionlimit() ) )

print( "n={} => n!={}".format( n, factorial( n ) ) )

if sys.getrecursionlimit() > m :
    print( "глубина рекурсии восстановлена в {}".format( m ) )
    sys.setrecursionlimit( m )