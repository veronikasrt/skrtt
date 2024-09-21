import math
def task1(rate, time, resolution):
    time = time * 60 #Перевод минут в секунды
    rate = rate * 1000 #Перевод кгц в гц с точкой
    v = (rate * time * resolution) / 8 #объем памяти в байт
    return int(v)

def task2(time1, resolution1, v1 ):
    time1 = time1 * 60 #Перевод минуты в секунды
    v1 = v1 * (1024 ** 2) #Перевод мб в байт
    rate1 = v1 / (time1 * resolution1 * (8)) #Частота в гц
    return float(rate1)

def task3(v2, resolution2, rate2):
    v2 = v2 * (1024 ** 3) #Перевод гб в байт
    time2 = v2 / (rate2 * resolution2 * (8)) #Время звучания в секундах
    return float(time2)


def task4(v3, resolution3, rate3):
    v3 = v3 * 1024 #Перевод кб в байт
    rate3 = rate3 * 1000 #Перевод кгц в гц
    time3 = v3 / (rate3 * resolution3 * (8)) #Время звучания в секундах
    return float(time3)

def task5(rate4, time4, resolution4):
    time4 = time4 * 60 #Перевод минут в секунды
    rate4 = rate4 * 1000 #Перевод кгц в гц с точкой
    v4 = (rate4 * time4 * resolution4) / 8 #Объем памяти в байт
    return int(v4)


if __name__ == "__main__" :
    #rate = float(input("частота: "))
    #time =  int(input("время в минутах: "))
    #resolution = int(input("разрешение: "))   
    #print (task1(rate, time, resolution))
    #v1 = float(input("объем в мб (писать с точкой): "))
    #time1 =  int(input("время в минутах: "))
    #resolution1 = int(input("разрешение: "))   
    #print (task2(v1, time1, resolution1))
    #v2 = float(input("объем в гб (с точкой): "))
    #rate2 =  int(input("частота: "))
    #resolution2 = int(input("разрешение: "))   
    #print (task3(v2, rate2, resolution2))
    #v3 = float(input("объем в кб: "))
    #rate3 =  int(input("частота: "))
    #resolution3 = int(input("разрешение: "))   
    #print (task4(v3, rate3, resolution3))
    rate4 = int(input("частота: "))
    time4 =  int(input("время в минутах: "))
    resolution4 = int(input("разрешение: "))   
    print (task5(rate4, time4, resolution4))




