sentence=str(input(u'Введите ваше преложение: ')).split(';')
count=0
for i in sentence:
	if len(i)>count:
		count=len(i)
		word=i
print(u'Самое большое слово это:', word)