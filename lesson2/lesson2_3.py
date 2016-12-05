sentence=str(input(u'Введите ваше преложение: '))
#sentence=sentence.find(' ')
symbol=str(input(u'Введите разделитель: '))
sentence=sentence.split(symbol)
count=0
for i in sentence:
	if len(i)>count:
		count=len(i)
		word=i
print(u'Самое большое слово это:', word)