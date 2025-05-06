# cara membaca file eksternal
print("baca file txt dengan open")
file = open("contoh.txt","r") #"r" artinya read(membaca)
# file = open("contoh.txt","w") #"w" artinya write(menulis)

# cek status
print(f"apakah bisa di baca: {file.readable()}")
# print(f"apakah bisa di tulis: {file.writable()}")

# cek isi file
print(file.read())
# print(file.write())

# baca 1 per 1
# print(file.readline()) #bawaan setiap readline ada 1 enter dan 1 enter dibelakang teks eksternal
# print(file.readline(),end="") #end untuk hapus enter
# print(file.readline())

# baca semua
# print(file.readlines())

# semua file harus di close(tutup)
print(file.close()) #tutup
print(f"apakah sudah di tutup: {file.closed}")

# teknik membuka file dengan with
print("baca file txt dengan open")

with open("contoh.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah sudah di tutup: {file.closed}")
print(f"apakah sudah di tutup: {file.closed}")