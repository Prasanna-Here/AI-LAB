from sympy import symbols
from sympy.logic.boolalg import And,Not,Implies
from sympy.logic.inference import satisfiable

P,Q=symbols('P Q')

#KB ((p → q) and p)

kb=And(Implies(P,Q),P)

query=Q

# KB and not query
test=And(kb,Not(query))
result=not satisfiable(test) 

print(f"Does KB entail Q? {result}")
