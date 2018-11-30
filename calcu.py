print("Ноль в качестве знака операции завершит работу программы")
while True:
	s = input("Знак (+,-,*,/): ")
	if s == '0': break
	if s in ('+','-','*','/'):
		num_1 = float(input("Введите первое число:"))
		num_2 = float(input("Введите второе число:"))
		if s == '+':
			print("%.2f" % (num_1+num_2))
		elif s == '-':
			print("%.2f" % (num_1-num_2))
		elif s == '*':
			print("%.2f" % (num_1*num_2))
		elif s == '/':
			if num_2 != 0:
				print("%.2f" % (num_1/num_2))
			else:
				print("Деление на ноль!")
	else:
		print("Неверный знак операции!")
