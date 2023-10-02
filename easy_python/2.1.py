password = input("Введите пароль: ")
criteria1 = len(password) >= 8
criteria2 = any(char in "$#!?-_" for char in password)
criteria3 = any(char.isupper() for char in password)

result = all([criteria1, criteria2, criteria3])
print(result)