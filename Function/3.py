'''fungsi'''

# def fungsi(argument):
#   badan fungsi
#   return fungsi
#fungsi(parameter)

# operasi 2 bilangan dengan return
def operasiMtk(angka1,angka2):
    tambah = angka1+angka2
    minus = angka1-angka2
    kali = angka1*angka2
    pangkat = angka1**angka2
    bagi = angka1/angka2
    modulus = angka1%angka2

    return tambah,minus,kali,pangkat,bagi,modulus

tam,min,kal,pang,bag,modul = operasiMtk(9,8)

print(f"operasi tambah: {tam}")
print(f"operasi kurang: {min}")
print(f"operasi kali: {kal}")
print(f"operasi pangkat: {pang}")
print(f"operasi bagi: {bag}")
print(f"operasi modulus: {modul}")