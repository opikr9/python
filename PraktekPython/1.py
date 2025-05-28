from datetime import datetime,date
hari_ini = datetime.today()

tanggal = int(input('masukan tanggal lahir: '))
bulan = int(input('masukan bulan lahir: '))
tahun = int(input('masukan tahun lahir: '))

tanggal_lahir = date(tahun,bulan,tanggal)
print(hari_ini)
print(tanggal_lahir)

umur = hari_ini.year - tanggal_lahir.year
print(umur)