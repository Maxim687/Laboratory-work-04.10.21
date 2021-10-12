from statistics import mean
a =int(input("Введите число a:"))
b =int(input("Введите число b:"))
e = a * b
x = int(input("Введите число x:"))
z = e ** x + x ** 0,5
print("z = " + str(z))
N = [-5,-3,-1,1,3,5,7,9]
V = [1,3,5,7,9]
avarage=mean(V)
print("Найбільше число N:" + str(max (N)))
print("Середнє арифметичне додатніх чисел N:" + str(avarage))
K = [-5,-3,-1]
K.reverse()
print(K)