x = str(input('Введите предложение: '))

def word_split(*args, **kwargs):
    global x
    x = x.split()
    for i in x:
        s = print(i, '-', len(i))
    return s

word_split(x)