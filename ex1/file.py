# Напишите программу, которая будет на вход принимать число N
# и выводить числа от -N до N

def num_reng(a):

    for i in range(-a, a+1): 
        print(i)

num = int(input("Введите число: ")) 
   
result = num_reng(num)  
print(result)  