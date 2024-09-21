import math 
def int_fract(num): 
    int_part = "" 
    fract_part = "" 
    flag = False 
    for i in num: 
        if i == ",": 
            flag = True 
            continue 
        if flag == False: 
            int_part = int_part + i 
        else: 
            fract_part = fract_part + i 
    if flag == False: 
        return str(int_conv(int_part)) 
    else: 
        return str(int_conv(int_part)) +  "," + str(fract_conv(fract_part)) 
 
def int_conv(num): 
    index = len(num)-1 
    result = 0  
    for i in num:  
        result += int(i) * (2 ** index) 
        index -= 1  
    return str(result) 
 
 
def fract_conv(fract_part):  
    if int(fract_part) == 0: 
        return 0 
    result = "" 
    compose = str(fract_part) 
    while int(compose[-3:]) > 0: 
        compose = int(compose[-3:]) * 2 
        if compose >= 1000: 
            result = result + "1" 
        else:  
            result = result + "0" 
        compose = str(compose) 
    return result  
 
if __name__ == "__main__": 
    num = str(input("Введите двоичное число: ")) 
    print(int_fract(num))
