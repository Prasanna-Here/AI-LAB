def implies(p,q):
    return (not p) and q

def biconditional(p,q):
    return (p and q) or (not p and not q)

def evaluate_expressions(p,q,r):
    result1=p and q
    result2=p or q
    result3=not q
    result4=implies(p,q)
    result5=biconditional(p,r)
    print(f"P AND Q = {result1}")
    print(f"P OR Q = {result2}")
    print(f"\u00AC Q = {result3}")
    print(f"P → Q = {result4}")
    print(f"P ↔ R = {result5}")

if __name__=='__main__':
    p=True
    q=False
    r=True
    evaluate_expressions(p,q,r)

