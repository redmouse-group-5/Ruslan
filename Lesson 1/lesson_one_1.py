x=int(input('Введите число от 1 до 9: '))
if x>=1 and x<=3:
    s=str(input('Введите строку: '))
    n=int(input('Введите колличество повторов строки: '))
    for i in range(n):
        print(s)
elif x>=4 and x<=6:
    m=int(input('Введите степень: '))
    print(x**m)
elif x>=7 and x<=9:
    i = x+10
    while x < i:
        x = x+1
        print(x)
else:
    b = '"Ошибка что-то пошло не так..."'
    print(b * 5)