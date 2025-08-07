import random

while True:
    angka = int(input("masukan angka 1-3: "))
    komputer = random.randint(1,3)
    match angka:
        case x if x < komputer:
            print("angka terlalu kecil")
        case y if y > komputer:
            print("angka terlalu besar")
        case z if z == komputer:
            print("jawaban benar")
    lanjut = input("lanjut (y/n): ")
    if lanjut == "n":
        break
    