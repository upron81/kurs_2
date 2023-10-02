import math
a, b, c = [float(i) for i in input().split()]
pp = (a+b+c)/2
s = math.sqrt(pp*(pp-a)*(pp-b)*(pp-c))
print(f"Площадь: {s}; полупериметр: {pp}.")