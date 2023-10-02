c = [1, 2, 4, 8, 16, 32, 64][::-1]
w = {}
i=0
s = int(input("Введите сумму: ").strip())
while s!=0:
    if s<c[i]:
        i+=1
        continue
        print(849484849)
    if c[i] not in w:
        w[c[i]]=0
    w[c[i]]+=1
    s-=c[i]

print(f"Купюры на выдачу: {w}")