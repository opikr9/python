# w untuk overwrite: yang sebelumnya dihapus di tulis baru
with open("data1.txt",mode="w",encoding="utf-8") as file:
    print(file.write("halo hehe\n"))
    
with open("data1.txt",mode="w",encoding="utf-8") as file:
    print(file.write("timpa hehe")) #angka yang diprint adalah jumlah elemen yang di print beserta spasi koma dll

# a untuk append menambahkan di akhir tanpa overwrite
with open("data2.txt",mode="a",encoding="utf-8") as file:
    print(file.write("ini append 1\n"))

with open("data2.txt",mode="a",encoding="utf-8") as file:
    print(file.write("ini append 2"))

# r+ untuk menimpa sesuai panjang teks di data
with open("data3.txt",mode="r+",encoding="utf-8") as file:
    print(file.write("adios-1\n"))
    print(file.write("holla-2\n"))

with open("data3.txt",mode="r+",encoding="utf-8") as file:
    file.write("timpa")