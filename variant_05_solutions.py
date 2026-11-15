"""Пошук коренів функції за допомогою чисельних методів
Вельгач Віктор
ЕІР30
Варіант 5"""

from typing import Callable

#creating a started function
def f(x):
    return x**4-13*x**2+36-1/x
    
#changing function for iteration method(x=phi(x))
def phi(x, lam):
    return x-lam*f(x)   #f(x)=0; -lamda*f(x)=-lamda*0=0; -lam*f(x)+x=x phi(x)=x; !!!phi(x)=x-lam*f(x)!!!

def df(x):
    return 4*x**3-26*x+1/x**2

def solve_iteration():
    a=float(input('Enter a minimal value of x(value a): '))
    b=float(input('Enter a maximum value of x(value a): '))
    print('Задавайте значення е, щоб перший значущий знак був якомого далі після коми(5-ий знак і більше), для збільшення точності і відкидання однакових, але схожив коренів')
    e=float(input('Enter an accuracy of aproximation(0.00006): '))
    p=1
    l=0
    k=[]
    #Знаходження знаку після коми, на якому з'являється перша значуща цифра
    sign=e
    while sign<1 :
        sign*=10
        l+=1
    for i in range(round(0.67*(b-a))+1):
        m=0
        n=0
        x=a+i/0.6
        if x!=0:
            lam=1/df(x)
        print(x)
        while abs(x-m)>=e:
            if n>3000 or abs(x)>10**10 or x==0:
                x=' '
                break
            m=x #introducing a variable to store the previous value
            x=phi(x, lam)
            n+=1
            print('attempt: ',p, '   number of iteration; ', n,'   value of argument: ', x)
        p+=1
        if x!=' ' and x!=0:
            x=round(x,l-2)
            k.append(x)
        elif x==' ': 
            x=0
    print('Корені отримані з точністю до',l-2, "знака після коми \n Тому деякі числа можуть вказувати на один і той самий корінь")
    print('КорeHi рівняння: ', set(k))   
