get_sq=None
if input(": ")=="RECT":
    get_sq=lambda a,b: a*b
else:
    get_sq=lambda a,b: 2*(a+b)

a = int(input("a: "))
b = int(input("b: "))
print(get_sq(a,b))