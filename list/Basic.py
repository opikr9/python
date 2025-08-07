jumlah = int(input("Berapa jumlah mahasiswa? "))
data_mahasiswa = []
total_nilai = 0

for i in range(jumlah):
    nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
    nilai = int(input("Masukkan nilai: "))
    data_mahasiswa.append([nama, nilai])
    total_nilai += nilai

print("\n==========================")
print("Data Mahasiswa:")
for idx, item in enumerate(data_mahasiswa, start=1):
    print(f"{idx}. {item[0]} - {item[1]}\n")

print("Nilai Rata2")
rata2 = total_nilai / jumlah
print(f"{rata2}\n")

print(f"Nilai Terendah: {min(data_mahasiswa, key=lambda x:x[1])}")
print(f"Nilai Tertingi: {max(data_mahasiswa, key=lambda x:x[1])}")


# TODO:
# - Hitung rata-rata
# - Cari nilai tertinggi & mahasiswa-nya
# - Cari nilai terendah & mahasiswa-nya
