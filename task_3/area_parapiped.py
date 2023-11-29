# import math

l = float(input("Введіть довжину l, см: "))
h = float(input("Введіть висоту h, см: "))
w = float(input("Введіть ширину w, см: "))

s = (l*w + l*h + h*w) * 2

print("Площа прямокутного паралелепіпеда S =", str(s), "см2")
