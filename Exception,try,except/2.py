# exception adalah error yang terjadi saat runtime
from math import nan


while(True):
    angka = int(input("masukan angka: "))
    hasil = nan
    try:
        hasil = 10/angka
        print(f"hasil: {hasil}")
        lagi = input("lagi? (y/n): ")
        if lagi == 'n':
            break
    except:
        print(f"hasil: {hasil}")
        print(f"masukan input lain selain 0")
print("akhir program")

while(True):
    try:
        with open("data2.txt","r") as file:
            print(file.read())
            break
    except:
        print("data2.txt belum ada membuat file baru")
        with open("data2.txt","w",encoding="utf-8") as file:
            file.write("file baru")
            print("file baru")
            break
