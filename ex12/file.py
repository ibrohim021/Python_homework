# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21



def distanse(x1,y1,x2,y2):
    result = (x1 - y1)*2 + (x2 - y2)*2**0.5
    print("Расстояние между координатами 2х точек = ",result)


x1 = int(input("Введие число х1 - " ))
y1 = int(input("Введие число y1 - " ))
x2 = int(input("Введие число х2 - " ))
y2 = int(input("Введие число y2 - " ))

result  = distanse(x1,y1,x2,y2)


