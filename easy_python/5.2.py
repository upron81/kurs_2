arr=[]
while inp:=input(": "):
    arr.append(inp)
arr=[[int(j) for j in i.split()] for i in arr]
print(arr)