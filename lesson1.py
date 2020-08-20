
from colorama import init
from colorama import Fore, Back, Style

init()

print( Back.GREEN )

what = input( "Что делаем? (+, -): " )

print( Back.CYAN )

a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))

print( Back.MAGENTA )

if what == "+":
    c = a + b
    print("Результат " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
else:
    print("Выбрана неверная операция!")