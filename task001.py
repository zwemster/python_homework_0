# task001 Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x, y, z = map(int, input('Введи три числа через пробел:').split())
if not (x or y or z) == (not x and not y and not z):
    print('Получается, что истинно...')
else:
    print('Кажется, что-то пошло не так...')
