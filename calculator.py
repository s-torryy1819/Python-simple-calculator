# calculator

what = input("Что делаем? (+, -, %, **, /):")

a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))

if what == "/" and b == "0":
	c = a / b
	print("Деление на 0!")
elif what == "-":
	c = a - b
	print("Вот ваш результат:" + str(c))
elif what == "**":
	c = a**b
	print("Ваш результат:" + str(c))
elif what == "%":
	c = a % b
	print("Ваш результат:" + str(c))
elif what == "+":
	c = a + b
	print("Вот ваш результат:" + str(c))




# the second calculator
'''num1 = float(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
	print(num1 + num2)
if op == "-":
	print(num1 - num2)
if op == "/":
	print(num1 / num2)
else:
	print(num1 * num2)'''
