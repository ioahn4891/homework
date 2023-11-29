num = int(input("Введіть 5 значне число:"))

num_5 = num % 10
num_4 = num // 10 % 10
num_3 = num // 100 % 10
num_2 = num // 1000 % 10
num_1 = num // 10000

div_3 = num // 3
div_6 = num // 6

print("тисячі:", num_2)
print("сотені:", num_3)
print("десятки:", num_4)
print("одиниці:", num_5)

print ("трійок у числі:", div_3)
print ("шісток у числі:", div_6)