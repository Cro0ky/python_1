#task 1
num = int(input('Введите число: '))
print(num)
print(num + 1)
print(num + 2)
#task 2
a = 2
b = 9
c = 11
print(a + b + c)
#task 3
a = 3
V = a**3
S = 6 * (a**2)
print(f'Объем = {V}\nПлощадь плотной поверхности = {S}')
#task 4
a = 1
b = 1
f = 3 * (a + b)**3 + 275 * b**2 - 127 * a - 41
print(f)
#task 5
a = int(input('num: '))
print(f'Следующее за числом {a} является: {a + 1}')
print(f'Для числа {a} предыдущее число: {a - 1}')
#task 6
monitor = int(input('monitor: '))
block = int(input('block: '))
klava = int(input('klava: '))
mouse = int(input('mouse: '))
print((monitor + block + klava + mouse) * 3)
#task 7
a_1 = int(input('a_1: '))
d = int(input('d: '))
n = int(input('n: '))
print(a_1 + d * (n - 1))
#task 8
a = int(input('num:'))
print(a, a*2, a*3, a*4, a*5, sep='---')
#task 9
n = int(input('schoolniki: '))
k = int(input('mandarini: '))
k_s = k // n
k_m = k % n
print(k_s)
print(k_m)
#task 10
nn = int(input('kol-vo: '))
result = round(nn / 2)
print(result)
#task 11
mins = int(input('mins: '))
print(f'{mins} МИН - это {mins // 60} час {mins - ((mins // 60) * 60)} минут')
#task 12
n = int(input("Введите число 1 или 0: "))
print((n - 1) * -1)
#task 13
a = '''
       _~_
      (0 0)
     /  ⌄  \ 
    /(  _  )\ 
     ˆˆ   ˆˆ   ̭'''
n = int(input("Введите число: "))
print(a * n)
#task 14
a = int(input('num: '))
print(a // 10)
#task 15
mins = int(input('mins: '))
print(mins // 60, (mins - (mins // 60) * 60))
#task 16
a = int(input('num 1 or 0: '))
print()
#task 17
a = int(input('num: '))
print((a // 2) * 2 + 2)
#task 18
s = 109
v = int(input('speed: '))
t = int(input('hours: '))
print((t * v) - 109)
#task 19
h = int(input())
a = int(input())
b = int(input())
print((h - a) // (a - b) + 1)
