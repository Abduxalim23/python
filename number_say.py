import os
# raqamlarni so'zga shaklini topuvchi funksiya
def birlik_say(num):
    s = ""
    if num == '9':
        s = "to'qqiz "  
    elif num == '8':
        s = "sakkiz "
    elif num == '7':
        s = "yetti "
    elif num == '6':
        s = "olti "
    elif num == '5':
        s = "besh "
    elif num == '4':
        s = "to'rt "
    elif num == '3':
        s = "uch "
    elif num == '2':
        s = "ikki "
    elif num == '1':
        s = "bir "
    elif num == '0':
        s = ""
    return s

# ikki xonali sonlarni so'zga aylantirish
def onlik_say(num):
    s = ""
    if num == '9':
        s = "to'qson "  
    elif num == '8':
        s = "sakson "
    elif num == '7':
        s = "yetmish "
    elif num == '6':
        s = "oltimish "
    elif num == '5':
        s = "ellik "
    elif num == '4':
        s = "qirq "
    elif num == '3':
        s = "o'ttiz "
    elif num == '2':
        s = "yigirma "
    elif num == '1':
        s = "o'n "
    elif num == '0':
        s = ""
    return s

# 3 xonali sonlarni so'zga aylantirish
def yuzlar_say(num):
    natija = ""
    if num[0] == "0" and num[1] == "0" and num[2] == "0":
        natija = ""
    elif num[0] == "0" and num[1] == "0":
        natija = birlik_say(num[2])
    elif num[0] == "0":
        num.remove(num[0])
        natija = onlik_say(num[0]) + birlik_say(num[1])
    else:
        natija = birlik_say(num[0]) + "yuz " + onlik_say(num[1]) + birlik_say(num[2])
    
    return natija 
    
# 4 xonali sonlarni so'zga aylantirish
def minglar_say(num):
    natija = ""
    if num[0] == "0" and num[1] == "0" and num[2] == "0":
        num.remove(num[0])
        num.remove(num[0])
        num.remove(num[0])
        print(num)
        natija = yuzlar_say(num)
    else:
        minglar = yuzlar_say(num) + "ming "
        print(minglar)
        num.remove(num[0])
        num.remove(num[0])
        num.remove(num[0])
        print(num)
        natija = minglar + yuzlar_say(num)
    
    return natija
# 7 xonali sonlarni so'zga aylantirish
def million_say(num):
    natija = ""
    if num[0] == "0" and num[1] == "0" and num[2] =="0":
        num.remove(num[0])
        num.remove(num[0])
        num.remove(num[0])
        print(num)
        natija = minglar_say(num)
    else:
        million = yuzlar_say(num) + "million "
        print(million)
        num.remove(num[0])
        num.remove(num[0])
        num.remove(num[0])
        print(num)
        natija = million + minglar_say(num)
        
    return natija

def milliardlar(num):
    natija = ""
    if num[0] =="0" and num[1] == "0" and num[2] =="0":
        num.remove(num[0])
        num.remove(num[0])
        num.remove(num[0])
        print(num)
        natija = million_say(num)
    else:
        milliard = yuzlar_say(num) + "milliard "
        print(milliard)
        num.remove(num[0])
        num.remove(num[0])
        num.remove(num[0])
        print(num)
        natija = milliard + million_say(num)
       
    return natija

# main body 999,999,999,999
number = input("Enter number: ")
number = list(number)
while len(number) != 12:
    number.insert(0,"0")
print(number)
yuz = milliardlar(number)
print(yuz)