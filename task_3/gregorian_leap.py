year = int(input("Введіть рік в діапазоні від 1900 до 1_000_000: "))

if 1900 < year < 1_000_000:

    if year % 4 != 0:
        print(year, "is not leep year")
    elif year % 100 == 0:
        if year % 400 == 0:
            print(year, "is Leap Year!")
        else:
            print(year, "is not leep year")
    else:
        print(year, "is Leap Year!")

else:
    print("не вірний діапазон!!!")