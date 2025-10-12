# Eercici 1.
print(30 % 4 - 30 - 2 * 5)#si
print(5 // 2 - 5/2)#No ja que aqui hem dona -0,5 pero el o,5 esta bé.
print(10 - 10 / 2 * 0.25 + 5)#si
print(10 - 10 / (2 * 0.25)+ 5)#si

# Exercici 2.
print(7 // 2)#Si
print(7 % 2)#Si
print(0 % 5)#Si
print(7 * 10 - 50 % 3 * 4 + 9)#Si
print((7 * (10 - 5) % 3) * 4 + 9)#Si
print(8 + 7 * 3 + 4 * 6)#Si
print(16 * 6 - 3 * 2)#Si
print(8 + 7 * 4 // 27 * (3 - (4 - 1)))#Si
# Exercici 3.
print(3 > 4)#Si
print(3 <= 4)#Si
print((3 > 4) or (8 > 1))#Si
print(not((3 > 4) or (8 > 1)))#Si
print((3 > 4) and (8 > 1))#Si
print(not((3 > 4) and (8 > 1)))#si
print((3 > 4) and (not (8 > 1)))#Si
print(not(5 != 5))#Si
# Exercici 4.
import cmath

a= 10
b= 25
c= 40
d= 33
e= 14
f= 87
g= 5
M= 54
N= 2
P= 6
Q= 97
# Formulas
formula1 = 5*a+b
formula2= 5*(a+b)
formula3 = 5*a+5*b
formula4= (a/b)+(c/d)
formula5= (a+b)/(c+d)
formula6= (M/N)+P
formula7= M+(N/(P-Q))
formula8= (a*b)/(c*d)
formula9= cmath.sqrt(b**2 + c**2)
formulapositiva10= (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
formulanegativa10= (-b - cmath.sqrt(b**2 - 4*a*c))/ (2*a)
formula11= (a+b/c)/(d - e/f)
formula12= (a*b)/c*d + c/(f*g)
print(formula1)
print(formula2)
print(formula3)
print(formula4)
print(formula5)
print(formula6)
print(formula7)
print(formula8)
print(formula9)
print(formulapositiva10)
print(formulanegativa10)
print(formula11)
print(formula12)
