#a)
print("a)")

A=True
B=True
print((A or B) and not(A))

A=True
B=False
print((A or B) and not(A))

A=False
B=True
print((A or B) and not(A))

A=False
B=False
print((A or B) and not(A))

#b)
print("b)")
A=True
B=True
print(not(A or B) and B)

A=True
B=False
print(not(A or B) and B)

A=False
B=True
print(not(A or B) and B)

A=False
B=False
print(not(A or B) and B)

#c)
print("c)")

A=True
B=True
print(A or not(B))

A=True
B=False
print(A or not(B))

A=False
B=True
print(A or not(B))

A=False
B=False
print(A or not(B))

#d)
print("d)")
A=True
B=True
print(not((A and B) and (B or A)))

A=True
B=False
print(not((A and B) and (B or A)))

A=False
B=True
print(not((A and B) and (B or A)))

A=False
B=False
print(not((A and B) and (B or A)))