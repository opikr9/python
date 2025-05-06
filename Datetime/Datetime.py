import datetime as dt #as artinya sebagai dt mewakili datetime
import time as tm 
# p

# jamIni = tm.time()
# print(f"jam hari ini adalah {jamIni}")

# penghitung umur
hariIni = dt.date.today()
print(f"hari ini adalah tahun {hariIni}")

# input user
print("\nmasukan tanggal bulan tahun lahir anda : ")
tanggal = int(input("tanggal : "))
bulan   = int(input("bulan   : "))
tahun   = int(input("tahun   : "))
tanggalLahir = dt.date(tahun,bulan,tanggal)
print(f"ini adalah tanggal lahir anda {tanggalLahir}")

# operasi perhitungan
hariSisa = hariIni-tanggalLahir
tahunSisa = hariSisa.days // 365
bulanSisa = hariSisa.days // 30
print(f"anda sudah hidup selama dari sekarang tanggal : {hariIni} \n hari : {hariSisa}\n bulan : {bulanSisa} \n tahun : {tahunSisa}")
print(f"hari ini adalah hari {hariIni:%A}")