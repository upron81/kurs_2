d={"house": "дом", "river": "река"}
inp=input(": ").split()
for index, i in enumerate(inp):
    if i in d:
        inp[index]=d[i]
print(' '.join(inp))