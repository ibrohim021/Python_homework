# Напишите программу, 
# которая принимает на вход число и проверяет
# кратно ли оно 5 и 10 или 15, но не 30

def num(n):
    if n%5 == 0 or n%10 == 0 or n%15 == 0:
        print("Число кратно")
    else:
        print("Число не кратно")
    return n


n = int(input('введите число: '))

result = num(n)

print(result)