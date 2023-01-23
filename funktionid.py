from random import *
from sys import *

username_list = ["user1","user2","user3","user4"]
password_list = ["psw1","psw2","psw3","psw4"]
def password_generation(number_of_initials:int):


    str0=".,:;!_*-+()/#¤%&"
    str1 = '1234567890'
    str2 = 'mnbvcxzlkjhgfdsaqwertyuiop'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3 
    ls = list(str4)
    shuffle(ls)
    psword = ''.join([choice(ls) for x in range(number_of_initials)])
    print("Sinu loodud parool on: ", psword)
    return psword

    

def user_choises():
    print("Tere tulemast")
    while True:
        try:
            valik = int(input("\nKui soovite luua uue konto - sisestage-1,\nkui soovid sisse logida - sisesta-2,\nkui soovite väljuda - sisestage-3\n:  "))
        except:
            print("Sisesta number!")
        if valik == 2:
            user_login()
        elif valik == 1:
            user_reg()
            user_login()
        elif valik == 3:
            exit()

def user_login():
    username = input("\nsisesta oma kasutajanimi: \n")
    try:
        if username in username_list:
            a = username_list.index(username)
            for i in range(3):
                password = input("\nsisesta parool: \n")
                if password == password_list[a]:
                    print("Sisselogimine õnnestus!")
                    break
                else:
                    print("\nVale parool!",(1+i))
        else:
            print("Vale kasutajanimi!")
    except:
        print("VIGA!")

def user_reg():
    username = input("Sisesta uus kasutajanimi: \n")
    while username in username_list:
        print("See kasutajanimi on kasutusel! Palun vali teine!")
        username = input("sisestage uus kasutajanimi: \n")
    else:    
        username_list.append(username)
    password = input("Kui soovite luua parooli - sisestage-1,\nkui soovite kasutada oma parooli - sisestage-2.\n : ")
    if password == "1":
        try:
            num = int(input("Sisestage initsiaalide summa : "))
        except:
            print("Peate sisestama numbri!")
        password_generation(num)
        password_list.append(password_generation(num))
    elif password == "2":
        sala = input("Sisesta uus parool : \n")
        while password_control(sala) != True:
            sala = input("Sisesta uus parool : \n") 
            if password_control(sala) == True:
                password_list.append(sala)
    return password

def password_control(password:str):
    password = list(password)

    num = len(password)
    k = 0
    l = 0
    o = 0
    for i in range(num):
        if password[i].isdigit():
            k += 1
        else:
            k += 0
        if password[i].isupper():
            l += 1
        else:
            l += 0
        if password[i].isalpha() == True:
            o += 1
        else:
            o += 0
    if k > 0 and l > 0 and o > 0:
        return True
    else:
        print("Parool peab koosnema numbritest, tähtedest ja suurtähtedest!")
        return False


user_choises()
