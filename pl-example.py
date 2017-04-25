from pyswip import Functor, Variable, Query, call
assertz = Functor("assertz",1)
father = Functor("father",2)

call(assertz(father("mi","j")))
call(assertz(father("mi","g")))

X = Variable()
q = Query(father("mi", X))
while q.nextSolution():
  print "Hello,", X.value
q.closeQuery()
