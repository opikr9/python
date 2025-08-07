# Latihan lIst

print("Opik Store Phone")
hpPesanan = []

while True:
    namaHp = str(input("silahkan masukan nama hp : "))
    seriHp = str(input(f"silahkan masukan seri hp {namaHp} : "))

    hpDipesan = [namaHp,seriHp]
    hpPesanan.append(hpDipesan)
    for index,hpKeluar in enumerate(hpPesanan):
        print(f"{index+1}. pesanan yang dibuat \n Nama Hp : {hpKeluar[0]}, \n Seri Hp : {hpKeluar[1]}")
    
    # pengkondisian apakah mau menambah pesanan
    tambahPesanan = input("Apakah ingin menambah pesanan? (y/n): ")
    hapusPesanan = input("Apakah ingin menghapus pesanan? (y/n): ")

    if tambahPesanan == 'n':
        break
    elif hapusPesanan == 'y':
        hpPesanan.remove(hpDipesan)
print("Terimakasih Sudah Berbelanja Di Opik Store")