x=int(input('Введите число от 1 до 9: '))
def str_count(*args,**kwargs):
    s=str(input('Введите строку: '))
    n=int(input('Введите колличество повторов строки: '))
    for i in range(n):
        print(i)
    return i

def extent(*args, **kwargs):
    m=int(input('Введите степень: '))
    return x**m

def str_repeat(*args, **kwargs):
    global x
    for i in range(x):
        x = i+1
        print(x)
    return x

def str_error(*args, **kwargs):
    x = print('Ошибка что-то пошло не так...\n' * 5)
    return x

if x>=1 and x<=3:
    str_count()
elif x>=4 and x<=6:
    extent()
elif x>=7 and x<=9:
    str_repeat()
else:
    str_error()