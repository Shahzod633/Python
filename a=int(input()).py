
'''a, b, c, d=int(input()), int(input()), int(input()), int(input()),
if a <= b and a <= c and a <= d:
    print(a)
if b <= a and b <= c and b <= d:
    print(b)
if c <= a and c <= b and c <= d:
    print(c)
if d <= a and d <= b and d <= c:
    print(d)
if a==b and a <= c and a <= d:
    print(a)
if b==c and b <= c and b <= d:
    print(b)
if c==d and  c <= b and c <= d:
    print(c)'''
# Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель в следующем формате:
# Раз*Два*Три
''' sep1=input()
a=input()
b=input()
c=input()
print(a, b, c, sep=sep1) '''

#Арифметическая прогрессия 
'''a=int(input())
d=int(input())
n=int(input())
N=n-1
D=d*N
A=a+D
print(A) '''

# Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах
''' a=int(input())
h=a//60
m=a%60
print(a, 'мин - это', h, 'час', m, 'минут', sep=' ', end=".") '''


# оператор AND 
''' age = int(input('Сколько вам лет?: ')) 
grade = int(input('В каком классе вы учитесь?: '))
if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    '''
# оператор OR
'''city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')'''
# оператор NOT
''' age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')'''
# оператор NOT
''' age = int(input('Сколько вам лет?: '))
if not (age < 12):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')'''
'''river1 = 'Волга'
river2 = 'Эльба'

print(river1 == 'Буг' and river2 == 'Одер')
print(river2 != 'Эльба' or river1 != 'Лена')'''
# Напишите программу, которая принимает целое число Напишите программу, которая принимает целое число 
# x определяет  принадлежит ли данное число указанному промежутку -1-----17.
'''   a=int(input())
if -1<a<17:
    print('Принадлежит')
else:
    print('Не принадлежит')'''
# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам. -∞---(-3) и (7)---+∞.
'''a=int(input())
if a<=-3 or a>=7:
    print('Принадлежит')
else:
    print('Не принадлежит')'''
# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам. -30<a<-2 или 7<a<25.
'''a=int(input())
if -30<a<=-2 or 7<a<=25:
    print('Принадлежит')
else:
    print('Не принадлежит')'''
# Красивое число - это четырехзначное число, которое делится на 7 или 17. Напишите программу, которая принимает целое число и определяет, является ли оно красивым.
'''a=int(input())
n=a%7
k=a%17
if 999<a<10000 and (n==0 or k==0):  
    print('YES')
else:
    print('No')'''
# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.    
'''a=int(input())
b=int(input())
c=int(input())
if (a+b)>c and (a+c)>b and (b+c)>a:
    print('YES')
else:
    print('NO')'''
# Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным, то выведите «YES» (без кавычек), иначе выведите «NO» (без кавычек).
''' a=int(input())
if ((a%4)==0 and (a % 100) != 0) or a % 400 == 0:
    print('YES')
else:
    print("NO") '''
# Ход ладьи 

'''a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a==c or b==d :
    print('YES')
else:
    print('NO')'''
# Ход Короля 
'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
if -1 <= (a - c) <= 1 and -1 <= (b - d) <= 1:
    print('YES')
else:
    print('NO')'''

# if and elif and else
# Гонка спидстеров кто быстрее кого 
'''speed1=int(input())
speed2=int(input())
a=speed1
b=speed2
if a<b:
    print('YES')
elif a==b:
    print("Don't know")
elif a>b:
    print('NO')'''

# Вид треугольника Равнобедренный--Равносторонний-Разносторонний
''' a=int(input())
b=int(input())
c=int(input())
if a==b and b==c and a==c:
    print('Равносторонний')
elif a==b or a==c or b==c:
    print('Равнобедренный')
elif a!=b and b!=c and a!=c:
    print('Разносторонний') '''
 
#  Серединное число
''' a=int(input())
b=int(input())
c=int(input())
if (b<a and a<c) or (b>a and a>c) or (c<a and a<b) or (c>a and a>b):
    print(a)
elif (a<b and b<c) or (a>b and b>c) or (c<b and b<a) or (c>b and b>a):
    print(b)
elif (b<c and c<a) or (a<c and c<b) or (a>c and c>b) or (b>c and c>a):
    print(c)
'''

# Количество дней в Месяце 
'''a=int(input())
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("31")
elif a==2:
    print("28")
elif a==4 or a==6 or a==9 or a==11:
    print("30") '''

# Церемония взвешивания 
'''' a=int(input())
if 0<a<60:
    print("Легкий вес")
elif 60<=a<64:
    print("Первый полусредний вес")
elif 64<=a<69:
    print("Полусредний вес") '''

#Самописный калькулятор!!!
# the first project in python!!!
''' a=int(input())
b=int(input())
c=input()
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif b==0 and c=="/":
    print("На ноль делить нельзя!")
elif c!="+" and c!="-" and c!="*" and c!="/":
    print("Неверная операция")
elif c=="/":
    print(a/b) '''

#Цветовой микшер трех цветов
'''a=input()
b=input()
if a==b  and ((a=="красный" or a=="синий" or a=="желтый") or (b=="красный" or b=="желтый" or b=="синий")):
    print(a)
elif (a=="красный" and b=="синий") or (a=="синий" and b=="красный"):
    print("фиолетовый")
elif (a=="красный" and b=="желтый") or (a=="желтый" and  b=="красный"):
    print("оранжевый")
elif (a=="синий" and b=="желтый") or (a=="желтый" and b=="синий"):
    print("зеленый")
elif (a!="красный" or a!="синий" or a!="желтый") or (b!="красный" or b!="желтый" or b!="синий"):
    print("ошибка цвета") '''

#Цвета колеса рулетки 
'''a=int(input())
if a==0:
    print("зеленый")    
elif 1<=a<=10 and a%2!=0:
    print("красный")
elif 1<=a<=10 and a%2==0:
    print("черный")
elif 11<=a<=18 and a%2!=0:
    print("черный")
elif 11<=a<=18 and a%2==0:
    print("красный")
elif 19<=a<=28 and a%2!=0:
    print("красный")
elif 19<=a<=28 and a%2==0:
    print("черный")
elif 29<=a<=36 and a%2!=0:
    print("черный")
elif 29<=a<=36 and a%2==0:
    print("красный")
else:
    print("ошибка ввода") '''

#Пересечение отрезков 
'''a=int(input())
b=int(input())
a2=int(input())
b2=int(input())
if '''

# Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается, то выведите «YES» (без кавычек), иначе выведите «NO» (без кавычек).
''' a=int(input())
if (a%100)==0:
    print('YES')
else:
    print('NO')'''

#Заданы две клетки шахматной доски. Напишите программу, которая определяет, имеют ли указанные клетки один цвет или нет. Если они покрашены в один цвет, то выведите слово «YES» (без кавычек), а если в разные цвета, то «NO» (без кавычек).
''' a=int(input())
b=int(input())
c=int(input())
d=int(input())
if ((a+b+c+d)%2)==0:
    print('YES')
else:
    print('NO')'''

# Girls only  На вход программе подаётся натуральное число – возраст претендента и буква обозначающая пол m (мужчина) или f (женщина).
'''a=int(input())
b=input()
if (10<=a<=15) and b=="f":
    print('YES')
elif (a<10 or a>15)   and b=='f':
    print('NO')
elif b=='m':
    print('NO')'''

# Римские цифры 1-10
''' a=int(input())
if a==1:
    print('I')
elif a==2:
    print('II')
elif a==3:
    print('III')
elif a==4:
    print('IV')
elif a==5:
    print('V')
elif a==6:
    print('VI')
elif a==7:
    print('VII')
elif a==8:
    print('VIII')
elif a==9:
    print('IX')
elif a==10:
    print('X')
else:
    print('ошибка')'''

# YES or NO – вот в чём вопрос 
''' a=int(input())
if (a%2)!=0:
    print('YES')
elif ((a%2)==0) and (2<=a<5):
    print('NO')
elif  ((a%2)==0) and (6<=a<=20):
    print('YES')
elif ((a%2)==0) and (a>20):
    print('NO')'''

#Ход слона
'''a=int(input())
b=int(input())
c=int(input())
d=int(input())
if abs(a - c) == abs(b - d):
    print('YES')
else:
    print('NO')'''

# Ход коня
''' a=int(input())
b=int(input())
c=int(input())
d=int(input())
if abs((a - c) * (b - d)) == 2:
    print('YES')
else:
    print('NO')'''

# Ход ферзя 
'''a=int(input())
b=int(input())
c=int(input())
d=int(input())
if abs(a - c) == abs(b - d) or a == c or b == d:
    print('YES')
else:
    print('NO')'''


# Площадь треугольника
'''a=float(input())
b=float(input())
S=1/2*a*b
print(S)'''

# Две старушки идут навстречу друг другу с постоянными скоростями V1 и V2 км/ч. Определите, через какое время (в часах) старушки встретятся, если расстояние между ними равно S км.
''' S=float(input())
V1=float(input())
V2=float(input())
t=S/(V1+V2)
print(t) '''

# Обратное число  
''' a=float(input())
if a>0 or a<0:
    print(a**(-1))
else:
    print('Обратного числа не существует') '''

# 451 градус по Фаренгейту
''' a=float(input())
ts=(5/9)*(a-32)
print(ts) '''

# Dog age сколько лет собаке в человеческом возрасте
''' a=float(input())
if a>2:
    print(21+(4*(a-2)))
elif a==1 or a==2:
    print(a*10.5) '''

# Первая цифра после точки 
''' a=float(input())
b=int((a*10)%10)
print(b) '''

# Дробная часть цыфры
'''a=float(input())
b=((a*10)%10)/10 
print(b)'''

# Наибольшее и наименьшее
''' a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
mi=min(a,b,c,d,e)
ma=max(a,b,c,d,e)
print('Наименьшее число', '=', mi)
print('Наибольшее число =', ma) '''

# Абсолютная сумма 5 чисел Напишите программу, которая вычисляет сумму их модулей
''' a=abs((float(input())))
b=abs((float(input())))
c=abs((float(input())))
d=abs((float(input())))
e=abs((float(input())))
print(abs(a+b+c+d+e))  '''

# Интересное число 
''' a=int(float(input()))
a3 =a%10
a2 = a%100//10
a1 = a//100
mi=min(a3,a2,a1)
ma=max(a3,a2,a1)
if (ma-mi)==(a3+a2+a1-mi-ma):
    print('Число интересное')
else:
    print('Число неинтересное')'''

# range(100, 111) создаст очередь из чисел: 100, 101, 102 ... до 110
'''for a in range(100, 200):
a3 = a % 10
a2 = a % 100 // 10
a1 = a // 100
    
mi = min(a3, a2, a1)
ma = max(a3, a2, a1)
    
if (ma - mi) == (a3 + a2 + a1 - mi - ma):
    print(a, '— Число интересное')'''

# Сортировка трёх  от большего к меньшему
'''a=int(input())
b=int(input())
c=int(input())
mi=min(a,b,c)
ma=max(a,b,c)
mid=a+b+c-mi-ma
print(ma)
print(mid)
print(mi)'''

# Манхэттенское расстояние 
'''a1=int(input())
a2=int(input())
b1=int(input())
b2=int(input())
M=abs(a1-b1)+abs(a2-b2)
print(M)'''

# Тема string  и  методы строк
'''s='"Python is a great language!"'
b=', said Fred.'
d='"I '
h="don't"
c=' ever remember having this much fun before."'
print(str (s)+str (b)+str (d)+str (h)+str (c))'''

# What's Your Name? тема string  и  методы строк
'''a=str(input())
b=str(input())
print('Hello', a, b + "! You have just delved into Python")'''

# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
'''city1=str(input())
city2=str(input())
city3=str(input())
city1_length=int(len(city1))
city2_length=int(len(city2))
city3_length=int(len(city3))
city_w_mini_l=min(city1_length, city2_length, city3_length)
city_w_maxi_l=max(city1_length, city2_length, city3_length)
if city1_length==min(city1_length, city2_length, city3_length) and city2_length==max(city1_length, city2_length, city3_length):
    print(city1)
    print(city2)
elif city1_length==min(city1_length, city2_length, city3_length) and city3_length==max(city1_length, city2_length, city3_length):
    print(city1)
    print(city3)
elif city2_length==min(city1_length, city2_length, city3_length) and city1_length==max(city1_length, city2_length, city3_length):
    print(city2)
    print(city1)
elif city2_length==min(city1_length, city2_length, city3_length) and city3_length==max(city1_length, city2_length, city3_length):
    print(city2)
    print(city3)
elif city3_length==min(city1_length, city2_length, city3_length) and city1_length==max(city1_length, city2_length, city3_length):
    print(city3)
    print(city1)
elif city3_length==min(city1_length, city2_length, city3_length) and city2_length==max(city1_length, city2_length, city3_length):
    print(city3)
    print(city2)
'''

# Арифметические строки
'''a, b, c=len(input()), len(input()), len(input())
if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0 :
    print('YES')
else:
    print('NO')
'''
# Напишите программу, которая считывает одну строку, после чего выводит «YES» (без кавычек), если во введённой строке есть подстрока «синий», или «NO» (без кавычек) в противном случае.
'''a=input()
b='синий'
if b in a:
    print('YES')
else:
    print('NO')
'''

#Корректный email 
'''a=input()
if '@' in a and '.' in a:
    print("YES")
else:
    print("NO")
'''
# Напишите программу, определяющую площадь круга и длину окружности по заданному радиусу R
'''from math import sqrt, ceil, pi 
R=float(input())
S=pi*pow(R, 2)
C=2*pi*R
print(S)
print(C)
'''
#  На вход поступает число сумируйте пол и потолок для этого числа  
''''from math import ceil,  floor
a=float(input())
ca=ceil(a)
fa=floor(a)
print(ca+fa)
'''
# Евклидово расстояние 
'''from math import sqrt, pow
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
p=sqrt(pow((x1-x2), 2) + pow((y1-y2), 2))
print(p)
'''

#Тригонометрическое выражение
'''from math import pow, pi, sin, cos, tan, radians
x=radians(float(input()))
M=sin(x)+cos(x)+pow(tan(x), 2)
print(M)
'''

# Правильный многоугольник
'''from math import pow, pi, tan
n=int(input())
a=float(input())
S=((n*pow(a, 2))/(4*tan(pi/n)))
print(S)
'''

# Средние значения -- среднее арифметическое, среднее геометрическое, среднее гармоническое, среднее квадратичное чисел
'''from math import sqrt, pow
a=float(input())
b=float(input())
print((a+b)/2) #среднее арифметическое
print(sqrt(a*b)) #среднее геометрическое
print((2*a*b)/(a+b)) #среднее гармоническое
print(sqrt((pow(a,2)+pow(b,2))/2)) #среднее квадратичное
'''
# Квадратное уравнение 
'''from math import pow, sqrt
a=float(input())
b=float(input())
c=float(input())
# ax**2+bx+c=0
D=pow(b,2)-(4*a*c)
if D<0:
    print('Нет корней')
elif D==0:
    x=-(b/(2*a))
    print(x)
elif D>0:
    x1=(-b-sqrt(D))/(2*a)
    x2=(-b+sqrt(D))/(2*a)
    print(min(x1, x2))
    print(max(x1, x2))
    '''
# Последовательность символов
'''
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

'''
# Повторяй за мной 1
'''a=input()
b=int(input())
for i in range(b):
    print(a)'''


# Звёздный прямоугольник
'''a=int(input())
for i in range(a):
        print("*******************") '''


# Повторяй за мной 2
'''a=input()
for i in range(10):
    print(i, a)'''

# Квадрат числа
'''from math import sqrt, pow
a=int(input())
print('Квадрат числа', 0, "равен", 0 )
for j in range(a):
    print('Квадрат числа', j+1, "равен", int(pow(j+1,2)))'''

#Звёздный треугольник 
'''a=int(input())
for j in range(a+1):
    if a>j:
        b=a-j
        print('*' * b)
'''
# Популяция 
'''a=int(input())
b=int(input())
c=int(input())
for j in range(c):
    print(j+1, (a * (b / 100 + 1) ** j) )'''



# продолжение изучение команд for 
'''for j in range(1, 10):
    print(j)'''

# таблица умножение 
'''a=int(input())
for j in range(1, 11):
    print(a, 'x', j, '=', a*j )
'''

# Последовательность чисел 2 
'''a=int(input())
b=int(input())
for j in range(a, b+1):
    if j%10==9:
        print(j)
    elif  j%15==0:
        print(j)
    elif j%17==0:
        print(j)'''


# последовательность чисел 3
'''b=int(input())
for j in range(a, b+1):
    if a<b:
        print(j)
    else:
        break
if a>b:
    for j in range(a, b-1, -1):
            print(j)
elif a==b:
    print(a)
'''

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''a=int(input())
a3=a%10 # последняя цифра
a2=(a%100)//10 # вторая цифра
a1=(a//100) # первая цифра
print('Сумма цифр:', a1 + a2 + a3)
print('Произведение цифр:', a1 * a2 * a3)'''

'''a, b, c = int(input()), int(input()), int(input())
if (b < a < c) or (c < a < b): 
    print(a, '- среднее число')
elif (a < b < c) or (c < b < a): 
    print(b, '- среднее число') 
else: 
    print(c, '- среднее число')
'''
'''total = 0

for i in range(1, 6):
     total += i
     print(total, end='')'''

# Количество чисел которая последняя цыфра будет 4 или 9
'''from math import pow
count=0
a=int(input())
b=int(input())
for j in range(a, b+1):
    if pow(j, 3)%10==4 or pow(j,3)%10==9:
        count += 1
print(count)'''

'''a,b,c=map(int, input().split())
print('a=', a, '\n', 'b=', b, '\n', 'c=', c, sep='')'''

# ОКругление до 3 знаков после запятой
'''x=95645.5466
print(f'x={x:9.3f}')
'''

# Обмен Валюти 
'''a=input()
b=9.6
if a=='usd':        # доллар -> Сомони
    c=int(input())
    print(b*c)
elif a=="som":
    c=int(input())
    print(c/b)      #Сомони -> доллар '''
# Расчет времени пути  
'''S=int(input('Растояние: '  'км'))
V=int(input('Cр скорость: '  'км/ч'))
t=S/V
print(t, 'часов')
'''
# площадь и периметр прямоугольника 
'''a=float(input())
b=float(input())
S=a*b
P=(a+b)*2
print('для забора нужно купить', P, 'забора' )
print('Плошадь равно', S 'метр квадрат')
'''
# Разделение яблок 
'''a, b=map(int, input().split())
f=a//b; d=b%a
print('студент=', f)
print('остаток=', d)'''

# Асимптотическое приближение
'''from math import log 
counter = 0
n = int(input())
for i in range(1, n+1):
    counter = counter + 1/i
print(counter - log(n))'''


# На вход программе подаётся натуральное число n Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно), , квадрат которых оканчивается на 2 на  5  или на 8.
'''from math import pow
n=int(input())
counter=0
for j in range(1, n+1):
    if pow(j,2)%10==2 or pow(j,2)%10==5 or pow(j,2)%10==8:
        counter+=j
print(counter)'''

# Факториал
'''n=int(input())
counter=1
for j in range(1, n+1):
    counter = counter*j
print(counter)'''

# Сумма делителей
'''n=int(input())
total=0
for j in range(1,n+1):
    if n%j==0:
        total+=j
    
print(total)'''

#  Напишите программу, которая считывает последовательность из 10 целых чисел и определяет, является ли каждое из них чётным или нет.
'''total=0
for _ in range(10):
    num=int(input())
    if num%2==0:
        total+=1
        if total==10:
            print("YES")
    elif num%2!=0:
        print("NO")
        break '''
# Знакочередующаяся сумма
'''n=int(input())
total=0
Total=0
for j in range(1, n+1):
    if j%2==0:
        total+=j
    else:
        Total+=j
print(Total-total)
    '''

# Наибольшое число 2 
'''n=int(input())
max1=0
max2=0
for j in range(n):
    num=int(input())
    if num>max1:
        max2=max1
        max1=num
    elif num>max2:
        max2=num
print(max1)
print(max2)'''

# Число Фибоначи 
'''n=int(input())
x=1
y=0
for j in range(1, n+1):
    print(x,end=' ')
    x,y=x+y,x'''

# Цикл while 1
'''num = int(input())
while num != -1:
    print('Квадрат вашего числа равен:', num * num)
    num = int(input())'''
    
# While 2
'''text = input()
total = 0
while text != 'stop':
    total += int(text)
    text = input()

print('Сумма чисел равна', total)
'''
# Бесконечный цикл
'''i = 0
while i < 10:
    print('Hello')'''

# До КОНЦА 1
'''text=input()
while text!="КОНЕЦ":
    print(text)
    text=input()
 '''

#До КОНЦА 2
'''text=input()
while text!="КОНЕЦ" and text!="конец":
    print(text)
    text=input()'''

# На вход программе подаётся последовательность слов, каждое слово на отдельной строке. Концом последовательности является одно из трёх слов: «стоп», «хватит», «достаточно» (без кавычек). Сами эти слова в последовательность не входят, лишь символизируя её окончание. Напишите программу, которая выводит общее количество членов данной последовательности.
'''ext=input()
total=0
while text!='стоп' and text!='хватит' and text!='достаточно':
    total+=1
    text=input()
print(total)'''

# а вход программе подаётся последовательность целых чисел делящихся на 7, каждое число на отдельной строке. Концом последовательности является любое число, не делящееся на 7 (само это число в последовательность не входит, лишь символизируя её конец). Напишите программу, которая выводит члены данной последовательности.
'''a=int(input())
while a%7==0:
    print(a)
    a=int(input())'''

# Сумма чисел
'''a=int(input())
total=0
while a>=0: 
    total+=a
    a=int(input())
print(total)'''

# Количество пятёрок  5
'''a=int(input())
total=0
while a>0 and a<6:
    if a==5:
        total+=1
    a=int(input())
print(total)'''

# У Тимура есть список никнеймов соцсети FriendsGram. Напишите программу, которая выводит первый никнейм, не содержащий символ нижнего подчёркивания _
'''=input()
while "_" in :
    =input()
while '_' not in :
    print()
    break'''
    
    
'''s='Информатика'
print(len(s))
print(s[:-6:-1])
'''
# Ведьмаку заплатите чеканной монетой В мире ведьмака существуют монеты с номиналами 1,5,10,25 Напишите программу, которая определяет, какое минимальное количество чеканных монет нужно заплатить ведьмаку.
'''a=int(input())
total=0
while a>=25: 
    total+=1
    a-=25
while a>=10:
    total+=1
    a-=10
while a>=5:
    total+=1
    a-=5
while a>=1:
    total+=1
    a-=1
print(total)'''

# Временной промежуток 
'''h=int(input())
m=int(input())
h1=int(input())
m1=int(input())
start=h*60+m
stop=h1*60+m1
if h<10 or m<10:
    print("%02d:%02d" % (h,m))
else:
    print(h,m, sep=":")
while start!=stop:
    start+=1
    h3=start//60
    m3=start%60
    if h3<10 or m3<10:
        print("%02d:%02d" % (h3,m3))
    else:
        print(h3,m3, sep=':')
'''
# Семь в числе
'''num = 1576
has_seven = False                                 # сигнальная метка (флаг)

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')'''


# Обратный порядок 1
'''a=int(input())
while a!=0:
    last_d= a%10
    print(last_d)
    a //= 10
'''

# Обратный порядок 2 
'''a=int(input())
while a!=0:
    l_dig = a%10
    print(l_dig, end='')
    a //=10'''

# max и min
'''maax=0
miin=9
last=0
n=int(input())
while n>0:
      last=n%10
      if last>maax:
          maax=last
      if last<miin:
          miin=last
      n =n//10
print('Максимальная цифра равна', maax)
print('Минимальная цифра равна', miin)   '''

# Дано натуральное число. Напишите программу, которая вычисляет: сумму его цифр; произведение его цифр; среднее арифметическое его цифр; его первую цифру; сумму его первой и последней цифры.
'''total=0         
summ=0            
proi=1          
A=0             
f=0             
n=int(input())
nl=n%10
while n!=0:
    last_d = n%10
    total += 1
    summ += last_d
    proi *= last_d
    n //= 10
A=summ/total
f=f+last_d+nl
print(summ)
print(total)
print(proi)
print(A)
print(last_d)
print(f)  '''   

# вторая цифра  Напишите программу, которая определяет его вторую (с начала) цифру.
'''a=int(input())
while a>9:
    last_d=a%10
    a //= 10
print(last_d)'''

# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
'''maax=0
miin=9
last=0
n=int(input())
while n>0:
      last=n%10
      if last>maax:
          maax=last
      if last<miin:
          miin=last
      n =n//10
      if maax!=miin:
        print('NO')
        break
if maax==miin:
    print('YES')'''

# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
'''a=int(input())
while a!=0:
    digit=a%10
    a //=10
    Sdigit=a%10
    if Sdigit==0:
        print('YES')
        break
    if Sdigit<digit:
        print('NO')
        break
        '''
# Четные цифры 2
'''a=int(input())
total=0
while a!=0:
    digit=a%10
    if digit%2==0:
        total+=1
        print(str(total)+"-"+'я четная цифра равна', digit)
    a//=10
if total==0:
    print('Четных цифр в числе нет') '''

# Четные цифры 3
'''n = input()
total = 0
for digit_str in n:
    digit = int(digit_str)
    if digit%2==0:
        total+=1
        print(str(total)+"-"+'я четная цифра равна', digit)
if total==0:
    print('Четных цифр в числе нет')
        '''

# Наименьший делитель
'''a=int(input())
for j in range(2, a+1):
        if a%j==0:
            print(j)
            break'''

# На вход программе подаётся натуральное число n Напишите программу, которая выводит числа от 1 до n включительно, за исключением:чисел от 5 до 9 включительно; чисел от 17 до 37 включительно; чисел от 78 до 87 включительно.
'''a=int(input())
for j in range(1, a+1):
    if 5<=j<=9:
        continue
    elif 17<=j<=37:
        continue
    elif 78<=j<=87:
        continue
    else:
        print(j)'''

# This program uses nested loops to print all the possible combinations of hours, minutes, and seconds in a day.
'''for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)'''

 # Таблица-1
'''a=int(input())
for i in range(a):
    for j in range(3):
        print(a, end=' ')
    print()'''

# Таблица-2 
'''a=int(input())
total=0
for i in range(1,a+1):
  for j in range(1, 6):
    print(i, end=" ") 
  print()'''

# Таблица-3
'''a=int(input())
for i in range(1, a+1):
  for j in range(1, 10):
    print(i, '+', j, '=', i+j)
  print()
'''
# Численный треугольник 
'''a=int(input())
for i in range(1):
  for j in range(1, a+1):
    print(str(j)*j)
  print()'''

# Звёздный треугольник
'''n = int(input())
mid = n // 2 + 1
count = 0

for i in range(1, n + 1):
    if i <= mid:
        count += 1 
    else:
        count -= 1
    
    print('*' * count) '''

# Сумма факториалов 
'''from math import factorial 
n=int(input())
total_sum = sum(factorial(i) for i in range(1, n + 1))
print(total_sum)'''        
        
# Подставь и узнаешь
'''n = int(input())
m = int(input())
solution = False
for emoji1 in range(1, n):
    for emoji2 in range(1, n):
        for emoji3 in range(1, n):
            if emoji1 + 3 * emoji2 + 2 * emoji3 == m:
                print(f"{emoji1} + 3×{emoji2} + 2×{emoji3} = {m}")
                solution = True
if not solution:
    print("При заданных n и m решений не существует.")'''
 
# Делители-2 
'''a = int(input())
b = int(input())
max_sum = 0
best_num = 0
for i in range(a, b + 1):
    current_sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            current_sum += j
    if current_sum >= max_sum:
        max_sum = current_sum
        best_num = i
print(best_num, max_sum)'''


# Численный треугольник 3
'''n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()'''

# Красивое время
'''n = int(input())
for h in range(24):
    m = h**n
    if 0 <= m < 60:
        print(f"{h:02}:{m:02}")'''

# Цифровой корень
'''n = int(input())
while n > 9:
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10  # Берем последнюю цифру
        n //= 10              # Отбрасываем последнюю цифру
    n = sum_digits

print(n)'''

#1
'''x=int(input())
y=int(input())
if x>0 and y>0:
    print('1-я четверьт')
elif x<0 and y<0:
    print('3-я четверьт')
elif x>0 and y<0:
    print('4-я четверьт')
else:
    print('2-я четверьт')'''


# 2
'''a='@$123976_$'
b=input()
if b in a:
    print('Доступ разрешен')
else:
    print('Доступ запрешен')'''

# 3
'''for j in range(1, 11):
    print(j, end=" ")'''

'''s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')
'''

# На вход программе подаются три строки: имя, фамилия и отчество (именно в таком порядке). Напишите программу, которая выводит инициалы человека.
'''a=input()   #имя 
b=input()   #фамилия
c=input()   #отчество
for j in range(len(b)):
    print(b[0], end='')
    break
for i in range(len(a)):
    print(a[i], end='')
    break
for x in range(len(c)):
    print(c[x])
    break'''

'''a=input()
print(a[2])
print(a[-2])
print(a[:5])
print(a[0:-2])
print(a[0::2])
print(a[:])
print(a[:0:-2])  # все символы строки через один в обратном порядке, начиная с последнего.
'''

'''"""
Моделирование движения планет
==============================
Физика: закон гравитации Ньютона  F = G * m1 * m2 / r^2
Интегратор: метод Верле (Velocity Verlet) — сохраняет энергию
Единицы: астрономические (а.е., годы, массы Солнца)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass, field

# ── Константы ────────────────────────────────────────────────────────────────
G = 4 * np.pi**2          # гравитационная постоянная в единицах [а.е.³ / (M☉ · год²)]

# ── Тело (планета или звезда) ────────────────────────────────────────────────
@dataclass
class Body:
    name:  str
    mass:  float                          # в массах Солнца
    pos:   np.ndarray                     # [x, y] в а.е.
    vel:   np.ndarray                     # [vx, vy] в а.е./год
    color: str  = "white"
    size:  float = 6
    trail: list  = field(default_factory=list)  # история позиций

    def __post_init__(self):
        self.pos = np.array(self.pos, dtype=float)
        self.vel = np.array(self.vel, dtype=float)


# ── Начальные условия: Солнечная система (упрощённо) ─────────────────────────
def create_solar_system() -> list[Body]:
    """
    Скорости рассчитаны из условия круговой орбиты: v = sqrt(G*M/r).
    Для реализма можно заменить на реальные данные NASA Horizons.
    """
    bodies = [
        Body("Солнце",   1.0,    [0.0,   0.0],   [0.0,  0.0],    color="#FFD700", size=20),
        Body("Меркурий", 1.65e-7,[0.387, 0.0],   [0.0,  10.10],  color="#B5B5B5", size=4),
        Body("Венера",   2.45e-6,[0.723, 0.0],   [0.0,   7.39],  color="#E8C46A", size=6),
        Body("Земля",    3.00e-6,[1.0,   0.0],   [0.0,   6.28],  color="#4FC3F7", size=6),
        Body("Марс",     3.23e-7,[1.524, 0.0],   [0.0,   5.09],  color="#EF5350", size=5),
        Body("Юпитер",   9.55e-4,[5.203, 0.0],   [0.0,   2.76],  color="#F4A460", size=14),
        Body("Сатурн",   2.86e-4,[9.537, 0.0],   [0.0,   2.04],  color="#DAA520", size=12),
    ]
    return bodies


# ── Физика ───────────────────────────────────────────────────────────────────
def compute_accelerations(bodies: list[Body]) -> list[np.ndarray]:
    """Вычисляет ускорение каждого тела от всех остальных (закон Ньютона)."""
    n = len(bodies)
    accs = [np.zeros(2) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            r_vec = bodies[j].pos - bodies[i].pos
            dist  = np.linalg.norm(r_vec)
            if dist < 1e-10:          # защита от деления на ноль
                continue
            f_mag = G * bodies[i].mass * bodies[j].mass / dist**2
            f_vec = f_mag * r_vec / dist
            accs[i] += f_vec / bodies[i].mass
            accs[j] -= f_vec / bodies[j].mass
    return accs


def velocity_verlet_step(bodies: list[Body], accs_old: list[np.ndarray], dt: float):
    """Один шаг интегрирования методом Velocity Verlet."""
    # 1. Обновить позиции
    for body, a in zip(bodies, accs_old):
        body.pos += body.vel * dt + 0.5 * a * dt**2

    # 2. Вычислить новые ускорения
    accs_new = compute_accelerations(bodies)

    # 3. Обновить скорости
    for body, a_old, a_new in zip(bodies, accs_old, accs_new):
        body.vel += 0.5 * (a_old + a_new) * dt

    return accs_new


# ── Анимация ─────────────────────────────────────────────────────────────────
def run_simulation(
    bodies: list[Body],
    dt: float  = 0.005,      # шаг по времени (год)
    steps_per_frame: int = 5, # шагов физики на один кадр
    max_trail: int = 180,     # длина следа (кадры)
    view_size: float = 11.0,  # размер окна (а.е.)
):
    fig, ax = plt.subplots(figsize=(9, 9), facecolor="#0a0a1a")
    ax.set_facecolor("#0a0a1a")
    ax.set_xlim(-view_size, view_size)
    ax.set_ylim(-view_size, view_size)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Моделирование Солнечной системы", color="white",
                 fontsize=14, pad=12)

    # Графические объекты
    dots   = [ax.plot([], [], "o", color=b.color, ms=b.size,
                      zorder=3)[0] for b in bodies]
    trails = [ax.plot([], [], "-", color=b.color, lw=0.8, alpha=0.5,
                      zorder=2)[0] for b in bodies]
    labels = [ax.text(0, 0, b.name, color=b.color, fontsize=7,
                      ha="left", va="bottom", zorder=4) for b in bodies]

    time_text = ax.text(0.02, 0.97, "", transform=ax.transAxes,
                        color="white", fontsize=10, va="top")

    # Предвычисляем начальные ускорения
    accs = compute_accelerations(bodies)
    elapsed = [0.0]   # мутабельный счётчик времени

    def init():
        for d in dots:   d.set_data([], [])
        for t in trails: t.set_data([], [])
        return dots + trails + labels + [time_text]

    def update(_frame):
        nonlocal accs
        for _ in range(steps_per_frame):
            accs = velocity_verlet_step(bodies, accs, dt)
            elapsed[0] += dt
            for body in bodies:
                body.trail.append(body.pos.copy())
                if len(body.trail) > max_trail:
                    body.trail.pop(0)

        for i, body in enumerate(bodies):
            dots[i].set_data([body.pos[0]], [body.pos[1]])
            if len(body.trail) > 1:
                tr = np.array(body.trail)
                trails[i].set_data(tr[:, 0], tr[:, 1])
            labels[i].set_position((body.pos[0] + 0.15, body.pos[1] + 0.15))

        years  = int(elapsed[0])
        days   = int((elapsed[0] - years) * 365.25)
        time_text.set_text(f"Время: {years} лет {days} дней")
        return dots + trails + labels + [time_text]

    ani = animation.FuncAnimation(
        fig, update, init_func=init,
        interval=20, blit=True, cache_frame_data=False
    )

    plt.tight_layout()
    plt.show()
    return ani


# ── Энтрипоинт ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("🪐 Запуск симуляции Солнечной системы...")
    print("   Закрой окно, чтобы остановить.\n")
    solar_system = create_solar_system()
    run_simulation(solar_system)'''

'''a=input()
print(a[2])
print(a[-2])
print(a[:5])
print(a[0:-2])
print(a[0::2])
print(a[:])
print(a[:0:-2])  # все символы строки через один в обратном порядке, начиная с последнего.'''

# Количество слов
'''a = input()
print(a.count(' ') + 1)'''

# время 
'''S=float(input('Растояние:'))
V=float(input('Скорость:'))
t=S/V
T=t%10
print(f'Время в дороге {t}часов')'''




















    
    


