from colorama import init
from colorama import Fore, Back, Style
import calendar

init()

print( Back.CYAN )
print( calendar.month(2019, 7))

print( Back.RED )

what = input("Что будем делать? (+,-,/,*): ")

print( Back.GREEN )

a = float(input("Введите первое число: "))

print( Back.YELLOW )

b = float(input("Введите второе число: "))

print( Back.MAGENTA )

if what == "+":
	c = a + b
	print("Результат: " + str(c))

elif what == "-":
	c = a - b
	print("Результат: " + str(c))

elif what == "/":
	c = a / b
	print('Результат: ' + str(c))

elif what == '*':
	c = a * b
	print('Результат: ' + str(c))

else:
	print('Неправильный ввод')

input()