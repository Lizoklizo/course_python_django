# Задача 1
# Напишите программу, которая выводит чётные числа из
# заданного списка и останавливается, если встречает число 237.
print("Задание 1.1")
data = [1, 12, 45, 12, 18, 34, 1, 3, 237, 22, 24]

for num in data:
    if num == 237:
        break
    if num % 2 == 0:
        print(num)

# Задача 2
# Ввести произвольное число в консоле
# Ввести пограничное число в консоле
# Если 1-ое число меньше пограничного, вывести сообщение об этом.
# Если 1-ое число больше пограничного, вывести сообщение об этом.
# Если 1-ое число больше пограничного более, чем в 3 раза, сообщить об этом

print("Задание 1.2")
n1 = int(input("Введите число: "))
n2 = int(input("Введите пограничное число: "))

if (n1 < n2):
    print("Произвольное число меньше пограничного")
elif (n1 > n2):
    print("Произвольное число больше пограничного")
    if (n1 > n2 * 3):
        print("Произвольное число более чем в 3 раза больше пограничного")