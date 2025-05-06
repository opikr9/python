# import package
# import package.matematika

# hasil = package.fisika.tambah(9,3)
# print(f"hasil tambah adalah: {hasil}")

# hasil = package.fisika.kali(9,5)
# print(f"hasil kali adalah: {hasil}")

# hasil = package.fisika.gaya(9,3)
# print(f"hasil gaya adalah: {hasil}")

# hasil = package.matematika.sains.pangkat(2)
# print(f"hasil pangkat adalah: {hasil(9)}")

# untuk semua (all)
from package import *
from package.matematika import *
hasil = fisika.tambah(9,3)
print(f"hasil tambah adalah: {hasil}")

hasil = fisika.kali(9,5)
print(f"hasil kali adalah: {hasil}")

hasil = fisika.gaya(9,3)
print(f"hasil gaya adalah: {hasil}")

hasil = sains.pangkat(2)
print(f"hasil pangkat adalah: {hasil(9)}")