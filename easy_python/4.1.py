names = [i for i in input(": ").split()]
i=0
while i!=len(names):
    if names[i].lower()[0] == names[i].lower()[-1]:
        print("Да")
        break
    i+=1
else:
    print("Нет")