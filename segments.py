
a1 = int(input())  # первый отрезок
b1 = int(input())
a2 = int(input())   # второй отрезок
b2 = int(input())

if a2 > b1:
    print("пустое множество")
elif a1 < a2 < b1 < b2:
    print(a2, b1)
elif b1 == a2 and b2 > b1 and a2 > a1:
    print(b1)
elif b1 == b2 and a1 == a2:
    print(a1, b1)  # 4 вариант
elif a2 < a1 < b2 and b1 >b2:
    print(a1, b2)
elif a1 > b2:  # 6 пункт
    print("пустое множество")
elif b2 > b1 and a1 > a2:
    print(a1, b1)
elif b1 > b2 and a2 > a1:
    print(a2, b2)
elif a1 == b2 and b1 > a1 > a2:
    print(a1)
elif b1 == b2 and a1 > a2:  #10 пункт
    print(a1, b1)
elif a1 == a2 and b2 > b1:
    print(a1, b1)
elif b1 == b2 and a2 > a1:  #12 вариант
    print(a2, b2)
elif a2 == a1 and b1 > b2:
    print(a2 - b2)


