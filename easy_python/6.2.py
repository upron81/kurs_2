names=[]
while inp:=input(": "):
    names.append(inp)
print(f"Число гостей {len(set(names))}.")