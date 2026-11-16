"""Пошук коренів функції за допомогою чисельних методів
Вельгач Віктор
ЕІР30
Варіант 5"""

def o():
    0

#creating a started function
def f(x):
    return x**4-13*x**2+36-1/x

#derivative of f(x)
def df(x):
    return 4*x**3-26*x+1/x**2

#changing function for iteration method(x=phi(x))
def phi(x, lam):
    return x-lam*f(x)   #f(x)=0; -lamda*f(x)=-lamda*0=0; -lam*f(x)+x=x phi(x)=x; !!!phi(x)=x-lam*f(x)!!!

def solve_iteration():
    print(''' \nЯкщо хочете знайти точні корені,
запустіть програму з широким околом навколо нуля,
потім подивіться приблизні значення коренів,
і наступного разу запустіть програму з вужчим околом,
який відповідає крайнім значенням коренів
та поставте дуже мале значення точності(е)\n''')
    a=float(input('Enter a minimal value of x(value a): '))
    b=float(input('Enter a maximum value of x(value a): '))
    section=int(input('Enter а number of sections into which we will divide the segment AB: '))
    print('''\nЗадавайте значення е,
щоб перший значущий знак був якомого далі після коми(5-ий знак і більше),
для збільшення точності і відкидання однакових, але схожив коренів\n''')
    e=float(input('Enter an accuracy of aproximation(0.00006): '))
    attempt=1
    global root
    root=[]
    global table
    table=[]
    
    #Знаходження знаку після коми, на якому з'являється перша значуща цифра
    sign=e
    l=0
    while sign<1 :
        sign*=10
        l+=1
        
    for i in range(section+1):
        member=0
        iter_number=0
        x=a+i*(b-a)/section #Розбиття проміжку на section частин
        apr0=round(x,l-2)
        
        if x!=0 and df(x)!=0:
            lam=1/df(x)
            
        #Рядок нижче виводив початкову апроксимацію для поточної спроби
        #print(x)
        
        while abs(x-member)>=e:
            if iter_number>5000 or abs(x)>10**10 or x==0:
                x=' '
                break
            member=x #introducing a variable to store the previous value
            x=phi(x, lam)
            iter_number+=1
            #Рядок нижче виводить рядки з номером спроби, номером ітерації та поточним коренем 
            #print('attempt: ',attempt, '   number of iteration: ', iter_number,'   value of argument: ', x)

        if x!=' ' and x!=0:
            x=round(x,l-2)
            root.append(x)                    #table.append([p,'    ',apr0,'                         ', n,'       ',x])
            table.append([attempt, apr0, iter_number, x])
        elif x==' ': 
            x=0
        attempt+=1
    print('Корені отримані з точністю до',l-2, "-ого знака після коми\nТому деякі числа можуть вказувати на один і той самий корінь")
    print('Корeні рівняння: ', set(root))
    print('Спроба; початкова апроксимація на цій спробі; к-ть ітерацій; корінь')
    #Виведення списку-протоколу(кожен підсписок з нового рядку)
    for t in range(len(table)):
        print(table[t])


def save_results_to_file():
    with open('results.txt','w',encoding='utf-8') as file:
        file.write(f"{'Перелік коренів рівняння: ':<23}{set(root)}\n")
        file.write('')
        file.write(f"{'Спроба':<10}{'Початкова апроксимація на спробі':<35}{'К-ть ітерацій':<17}{'Корінь':<10}\n")
        for t in range(len(table)):
            file.write(f"{table[t][0]:<10}{table[t][1]:<35}{table[t][2]:<17}{table[t][3]:<10}\n")

#Точка входу(цю функцію треба викликати у консолі, щоб запустити програму)            
def main():
    solve_iteration()
    save_results_to_file()