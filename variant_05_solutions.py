"""Пошук коренів функції за допомогою чисельних методів
Вельгач Віктор
ЕІР30
Варіант 5"""

from typing import Callable

#creating a started function
def target_function(x):
    return x**4-13*x**2+36-1/x
    
#changing function for iteration method(x=phi(x))
def phi(x):
     return x**6-13*x**4+36*x**2   #f(x)=0; f(x)+x=x; phi(x)=x; !!!phi(x)=f(x)+x!!!

def solve_iteration():
     a=float(input('Enter a minimal value of x(value a): '))
     b=float(input('Enter a maximum value of x(value a): '))
     e=float(input('Enter an accuracy of aproximation(0.00006): '))
     p=1
     k=[]
     for i in range(round(11*(b-a))+1):
         m=0
         n=0
         x=a+i/10
         print(x)
         while abs(x-m)>=e:
             if n>300 or x>10**10 or x==0:
                 x=' '
                 break
             m=x #introducing a variable to store the previous value
             x=phi(x)
             n+=1
             print('attempt: ',p, '   number of iteration; ', n,'   value of argument: ', x)
         p+=1
         if x!=' ' and x!=0:
             k.append(x)
         elif x==' ': 
             x=0
     print('КорeHi рівняння: ', k)   
