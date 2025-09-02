def implies(p, q):
    return (not p) or q

def iff(p, q):
    return (p and q) or (not p and not q)

p,q,r = True,False,True

print("--proporstional logic--")
print("A and !c = ", p and not q)
print("(A and B) and c = ", (p and q) and r) 
print("!b or A = ", not q and p)
print("A implies C = ", implies(p, r))
print("B iff c = ", iff(q, r))
