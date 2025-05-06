# latihan function
import os
# Heading
def Judul():
    os.system("cls")
    print(f"{'Program Hitung Luas':^50}")
    print(f"{'Dan Keliling Persegi Panjang':^50}")
    print(f"{'-':^}"*50)
    return

# Input User
def inputUser():
    panjang = int(input("masukan panjang persegi panjang: "))
    lebar = int(input("masukan lebar persegi panjang: "))

    return panjang,lebar

# Hitung Luas
def hitungLuas(panjang,lebar):
    luas = panjang*lebar

    return luas

# Hitung Keliling
def hitungKeliling(panjang,lebar):
    keliling = 2*(panjang*lebar)

    return keliling

def display(message,value):
    '''MENAMPILKAN HASIL'''
    print(f"hasil perhitungan {message} = {value}")

while True:
    Judul()
    LEBAR,PANJANG = inputUser()
    LUAS = hitungLuas(PANJANG,LEBAR)
    KELILING = hitungKeliling(PANJANG,LEBAR)

    display("luas", LUAS)
    display("keliling", KELILING)

    lanjut = input("lanjutt? (y/n): ")
    if lanjut == 'n':
        break
print("program selesai")