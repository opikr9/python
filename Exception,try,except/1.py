# exception akan terjadi saat program mengalami error saat runtime

from math import nan

# contoh sederhana untuk menangkap exception

# contoh sederhana
# inputUser = int(input("masukan angka: "))
# hasil = nan

# try:
#     hasil = 10/inputUser
# except:
#     print("input tidak boleh 0")
# print(f"hasil: {hasil}")

# contoh di aplikasi
while(True):
    angka = int(input("masukan angka pembagi: "))
    try:
        hasil = 10/angka
        print(f"hasil: {hasil}")
        lagi = input("lagi (y/n): ")
        if lagi == 'n':
            break
    except:
        print("pembagi 0,masukan angka lain!")
print("akhir program 1")

while(True):
    try:
        with open("data.txt","r") as file:
            print(file.read())
            break
    except:
        print("file data.txt tidak ditemukan membuat file baru")
        with open("data.txt","w",encoding="utf-8") as file:
            file.write("file baru")
            break
print("akhir program 2")