print(u'Общество в начале XXI века')
x=int(input(u'Каков ваш возраст?'))
if x>=0 and x<=7:
    print(u'Вам в детский сад')
elif x>=7 and x<=18:
    print(u'Вам в школу')
elif x>=18 and x<=25:
    print(u'Вам в профессиональное учебное заведение')
elif x>=25 and x<=60:
    print(u'Вам на работу')
elif x>=60 and x<=120:
    print(u'Вам предоставляется выбор')
else:
    print(u'Ошибка эта программа для людей...')
