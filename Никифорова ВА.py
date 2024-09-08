import math

#def task7(a, b, c):
    #i = (a * b) / (2 ** c)
    #return int(i)

#if __name__ == "__main__":
    #inp1 = int(input("Количество белой краски: "))
    #inp2 = int(input("Количество синей краски: "))
    #inp3 = int(input("Количество бит: "))
    #print(task7(inp1, inp2, inp3))


    #def task18(a, b, c, d):
    #N = 2 ** (d / (a * b * c))
    #return int (N)

#if __name__ == "__main__":
    #inp1 = int (input("Количество страниц: "))
    #inp2 = int (input("Количество строк: "))
    #inp3 = int (input("Количество символов: "))
    #inp4 = int (input("Количество байт: "))
    #print(task18(inp1, inp2, inp3, inp4))


#def task19(a, b):
        #i = (math.log2(a))  / (math.log2(b))
        #return float(i)

#if __name__ == "__main__":
    #inp1 = float(input("Данные первого текста: "))
    #inp2 = float(input("Данные второго текста: "))
    #print(task19(inp1, inp2))


    #def task20(a, b):
    #i = a / (math.log2(b))
    #return int (i)

#if __name__ == "__main__":
    #inp1 = int (input("Количество бит: "))
    #inp2 = int (input("Количество символов: "))
    #print(task20(inp1, inp2))


    #def task19(a):
    #N = 2 ** a
    #return int (N)

#if __name__ == "__main__":
    #inp1 = int (input("Количество бит: "))
    #print(task19(inp1))


def task20(a):
    N = 2 ** a
    return int (N)

if __name__ == "__main__":
    inp1 = int (input("Количество бит: "))
    print(task20(inp1))