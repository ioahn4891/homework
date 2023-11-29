name = input("ваше ім'я:")
surname = input("ваше призвіще:")
age = int(input("ваш вік:"))
age = 100 - age

print ("\n Привіт,", surname, end=". ")
print("\n", name, "це гарне ім'я - мені подобається", end=".")
print("\n До 100 років тобі залишилося жити", age, "років")