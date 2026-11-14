"""Пошук коренів функції за допомогою чисельних методів
Вельгач Віктор
ЕІР30
Варіант 5"""

a=float(input('Enter a minimal value of x(value a): '))
b=float(input('Enter a maximum value of x(value a): '))
e=a=float(input('Enter an accuracy of aproximation(0.00006): '))

#creating a started function
def target_function(x):
    x**4-13*x**2+36-1/x
    
#changing function for iteration method(x=ph(x))
def phi(x):
    target_function(x)+x   #f(x)=0; f(x)+x=x; phi(x)=x; !!!phi(x)=f(x)+x!!!

    
