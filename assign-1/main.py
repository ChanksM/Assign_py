from uper import *
from symbol import *
from lenght import *
from number import *
import os

def main():
    Dict = {}
    while True:
        password = input("enter pass: ")
        if upp(password) != True:
            print("parolshi unda erios minimum 2 didi simbolo")
        elif length(password) == False:
            print("paroli sigrdze ararelevanturia")
        elif numbers(password) != True:
            print("parolshi unda erios minimum 2 cifri")
        elif symbols(password) == False:
            print("gamoyenebulia akrdzaluli simbolo")
        else:
            print("password confirmed")
            break

    Dict[os.urandom(2)] = password
    print(Dict)

if __name__ == "__main__":
    main()
