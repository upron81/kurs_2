a, b = [float(i) for i in input("Введите a, b: ").split()]
result = True if a>b*60 else False
print(f"A больше b: {result}")