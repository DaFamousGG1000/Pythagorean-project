from math import sqrt
from time import sleep
import subprocess
import os

def pythagoras() :
    from math import sqrt
    from time import sleep
    import os
    import subprocess
    
    formula = str(input("Silahkan Pilih sisi yang akan dihitung (a, b, c) >> "))

    if formula == "c" :
        for i in range (1) :
            side_a = int(input("Masukkan panjang sisi a >>"))
            side_b = int(input("Masukkan panjang sisi b >>"))
            side_c = sqrt(side_a * side_a + side_b * side_b)
            print("Panjang sisi c", side_c)
            sleep(1.25)

    if formula == "b" :
        for i in range (1) :
            side_c = int(input("Masukkan panjang sisi c >>"))
            side_a = int(input("Masukkan panjang sisi a >>"))

            side_b = sqrt(side_c * side_c - side_a * side_a)
        
            print("Panjang sisi b", side_b)
            sleep(1.25)
    if formula == "a" :
        for i in range (1) :
            side_c = int(input("Masukkan panjang sisi c >>"))
            side_b = int(input("Masukkan panjang sisi b >>"))

            side_a = sqrt(side_c * side_c - side_b * side_b)

            print("Panjang sisi a", side_a)
            sleep(1.25)
    if formula == "C" :
        for i in range (1) :
            side_a = int(input("Masukkan panjang sisi a >>"))
            side_b = int(input("Masukkan panjang sisi b >>"))
            side_c = sqrt(side_a * side_a + side_b * side_b)
            print("Panjang sisi c", side_c)
            sleep(1.25)

    if formula == "B" :
        for i in range (1) :
            side_c = int(input("Masukkan panjang sisi c >>"))
            side_a = int(input("Masukkan panjang sisi a >>"))

            side_b = sqrt(side_c * side_c - side_a * side_a)
        
            print("Panjang sisi b", side_b)
            sleep(1.25)
    if formula == "A" :
        for i in range (1) :
            side_c = int(input("Masukkan panjang sisi c >>"))
            side_b = int(input("Masukkan panjang sisi b >>"))

            side_a = sqrt(side_c * side_c - side_b * side_b)

            print("Panjang sisi a", side_a)
            sleep(1.25)

START = str(input("Apakah anda ingin memulai ? (Y/N)"))
if START == 'Y' :
    for i in range (1) :
        pythagoras()
if START == 'N' :
    exit()
if START == 'y' :
    for i in range (1) :
        pythagoras()
if START == 'n' :
    exit()
while True :
    restart = str(input("Apakah anda ingin mengulangi? >>"))
    
    while restart == 'N' :
        subprocess.call('cls', shell=True)
        exit()
    while restart == 'n' :
        subprocess.call('cls', shell=True)
        exit()
    if restart == 'Y' :
        subprocess.call('cls', shell=True)
        pythagoras()
    if restart == 'y' :
        subprocess.call('cls', shell=True)
        pythagoras()
    

