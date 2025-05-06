import datetime
import os
import string
import random
os.system("cls")

wadahWarga = {
    'nama':'nama',
    'id':000,
    'alamat':'alamat',
    'lahir':datetime.datetime(1999,12,1)
}

dataWarga = {}

print(f"{'INPUT DATA WARGA JATENG':<20}")

while True:
    Warga = dict.fromkeys(wadahWarga.keys())
    Warga['nama'] = input("Masukan Nama: ")
    Warga['id'] = int(input("Masukan Id: "))
    Warga['alamat'] = input("Masukan Alamat: ")
    tahunLahir = int(input("Masukan Tahun Lahir: "))
    bulanLahir = int(input("Masukan Bulan Lahir: "))
    tanggalLahir = int(input("Masukan Tanggal Lahir: "))
    Warga['lahir'] = datetime.datetime(tahunLahir,bulanLahir,tanggalLahir)
    key = ''.join({random.choice(string.ascii_uppercase) for i in range(6)})
    dataWarga.update({key:Warga})

    print(f"{'key':<5}{'nama':<15} {'id':<4} {'alamat':<12} {'lahir':<10}")

    for Warga in dataWarga:
        key = Warga

        nama = dataWarga[key]['nama']
        id = dataWarga[key]['id']
        alamat = dataWarga[key]['alamat']
        lahir = dataWarga[key]['lahir'].strftime("%x")

        print(f"{key:<5} {nama:<15} {id:<4} {alamat:<12} {lahir:<10}")

    lagi = input("lagi? (y/n): ")

    if lagi == 'n':
            break

print("done")