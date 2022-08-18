import sys
def returnSymbol(number):
    symbol_dict={
        1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',
        40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'
    }
    return symbol_dict[number]

def getRoman(dividend,number):
    quot,rem=number//dividend,number%dividend
    print(rem)
    roman=''
    for _ in range(quot):
        roman+=returnSymbol(dividend)
    if rem!=0:
        roman+=romanizer(rem)
    return roman

def romanizer(number):

    if(number<10):
        return returnSymbol(number)
    elif(number<40):
        return getRoman(10,number)
    elif(number<50):
        return getRoman(40,number)
    elif(number<90):
        return getRoman(50,number)
    elif(number<100):
        return getRoman(90,number) 
    elif(number<400):
        return getRoman(100,number)
    elif(number<500):
        return getRoman(400,number)
    elif(number<900):
        return getRoman(500,number)
    elif(number<1000):
        return getRoman(900,number)
    return ''

print("Program to convert decimals to Roman letters\tEnter 0 to exit.")
while True:
    number=int(input(">"))
    if number!=0:
        print(romanizer(number))
    else:
        sys.exit()