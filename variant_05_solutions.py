"""Пошук коренів функції за допомогою чисельних методів
Вельгач Віктор
ЕІР30
Варіант 5"""

#creating a started function
def f(x):
    return x**4-13*x**2+36-1/x
    
#changing function for iteration method(x=phi(x))
def phi(x, lam):
    return x-lam*f(x)   #f(x)=0; -lamda*f(x)=-lamda*0=0; -lam*f(x)+x=x phi(x)=x; !!!phi(x)=x-lam*f(x)!!!

def df(x):#derivative of f(x)

    return 4*x**3-26*x+1/x**2

def solve_iteration():
    a=float(input('Enter a minimal value of x(value a): '))
    b=float(input('Enter a maximum value of x(value a): '))
    print('Задавайте значення е, щоб перший значущий знак був якомого далі після коми(5-ий знак і більше), для збільшення точності і відкидання однакових, але схожив коренів')
    e=float(input('Enter an accuracy of aproximation(0.00006): '))
    p=1
    l=0
    k=[]
    global table
    table=[]
    
    #Знаходження знаку після коми, на якому з'являється перша значуща цифра
    sign=e
    while sign<1 :
        sign*=10
        l+=1
    for i in range(round(0.62*(b-a))+1):
        m=0
        n=0
        x=a+i/0.6
        apr0=round(x,l-2)
        
        if x!=0 and df(x)!=0:
            lam=1/df(x)
            
        #Рядок нижче виводив початкову апроксимацію для поточної спроби
        #print(x)
        
        while abs(x-m)>=e:
            if n>3000 or abs(x)>10**10 or x==0:
                x=' '
                break
            m=x #introducing a variable to store the previous value
            x=phi(x, lam)
            n+=1
            #Рядок нижче виводить рядки з номером спроби, номером ітерації та поточним коренем 
            #print('attempt: ',p, '   number of iteration; ', n,'   value of argument: ', x)

        if x!=' ' and x!=0:
            x=round(x,l-2)
            k.append(x)                    #table.append([p,'    ',apr0,'                         ', n,'       ',x])
            table.append([p, apr0, n, x])
        elif x==' ': 
            x=0
        p+=1
    print('Корені отримані з точністю до',l-2, "-ого знака після коми\nТому деякі числа можуть вказувати на один і той самий корінь")
    print('Корeні рівняння: ', set(k))
    print('Спроба; початкова апроксимація на цій спробі; к-ть ітерацій; корінь')
    #Виведення списку-протоколу(кожен підсписок з нового рядку)
    for t in range(len(table)):
        print(table[t])


def save_results_to_file():
    global table
    with open('results.txt','w',encoding='utf-8') as file:
        file.write(f"{'Спроба':<10}{'Поч. апроксим. на спробі':<27}{'К-ть ітерацій':<15}{'Корінь':<10}\n")
        for t in range(len(table)-1):
            file.write(f"{table[t][1]:<10}{table[t][2]:<10}{table[t][3]:<10}{table[t][4]:<10}\n")