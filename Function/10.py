# global scope
nama = "opik" #dari luar function
def globals(nama):
    return nama
print(f"panggil global {globals(nama)}")

# local scope
pisah = "adios"
def locals(pisah):
    return pisah
print(f"sebelum {pisah}")
locals(pisah)
print(f"sesudah {pisah}")

# cara memanggil global scope di local scope
combine = "local global"
def campur(baru):
    global combine
    combine = baru

    return baru
print(campur("halo"))

# kegunaan global di for dan if
angka = 0 #dari luar(global)

for i in range(0,3):
    angka += i

    print(f"angka sekarang {i}")

if True:
    angka += i

    print(angka)