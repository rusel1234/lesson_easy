# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
km = int(input('введите кол-во километров: '))
def convert(km):
    miles = km / 1.609
    print(miles)
convert(km)

# -2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
# def f(n=float(input("numerical request: "))):
if float(n) - int(n) > 0.5:
    print(int(n) + 1)
else:
    print(int(n))



# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)
sp = input()
if sp[0] + sp[1] + sp[2] == sp[3] + sp[4] + sp[5]:
    print('Счастливый')