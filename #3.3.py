import math
a = int(input('Введите коэффициент a: ')) 
b = int(input('Введите коэффициент b: ')) 
c = int(input('Введите коэффициент c: ')) 
 
d = (b**2) -(4*a*c)
if d>=0: 
    k1 =(-b- math.sqrt(d))/(2*a) 
    k2 =(-b+ math.sqrt(d))/(2*a) 
    print('x1= {0} ; x2= {1}'.format(k1,k2)) 
else:
    print("Дискриминант отрицателен, корней нет")
