import sys
barang = ["Buku","Pulpen","Penghapus","jupyter","keyboard","tws","handphone","powerbank","permen"]

def create_barang():
    if len(barang) >= 10:
            print("tidak bisa crud storage penuh!")
            sys.exit()
    else:
        tambah = input("masukan nama barang: ")
        barang.append(tambah)
        print("Barang berhasil ditambahkan")
        
def read_barang():
    print("Daftar barang")
    if not barang:
        print("Barang tidak ditemukan!")
    else:
        print(f"total barang: {len(barang)}")
        for index_barang, value_barang in enumerate(barang):
            print(f"{index_barang}, {value_barang}")

def update_barang():
    read_barang()
    try:
        update = int(input("pilih nomor barang: "))
        if 0 <= update < len(barang):
            barang_update = input("masukan nama barang baru: ")
            barang[update] = barang_update
            print("Barang berhasil di update")
        else:
            print("nomor tidak ditemukan")
    except ValueError:
        print("input harus angka!")

def delete_barang():
    read_barang()
    try:
        hpus = input("hapus 1/all: ").lower()
        if hpus == "1":
            hapus_index = int(input("masukan no barang untuk dihapus: "))
            if 0 <= hapus_index < len(barang):
                conf = input("hapus? (y/n): ")
                if conf == "y":
                    barang.pop(hapus_index)
                    print("barang berhasil dihapus")
                else:
                    print("gagal menghapus")
            else:
                print(f"barang {hapus_index} gagal dihapus")
        elif hpus == "all":
            hapus_all = input("hapus semua? (y/n: )")
            if hapus_all == "y":
                barang.clear()
    except:
        print("barang gagal dihapus")

def find_barang():
    find = input("masukan nama barang: ")
    if find in barang:
        print(f"barang ditemukan: {find}")
    else:
        print(f"{find} tidak ditemukan")

def sort_barang():
    barang.sort(key=str.lower)
    print(barang)

def main():
    while True:
        print("\n1. Tambah barang")
        print("2. Tampilkan barang")
        print("3. Update barang")
        print("4. Hapus barang")
        print("5. Cari barang")
        print("6. urutkan barang")
        print("7. exit")

        pilih = int(input("masukan pilihan: "))

        if pilih == 1:
            create_barang()
        elif pilih == 2:
            read_barang()
        elif pilih == 3:
            update_barang()
        elif pilih == 4:
            delete_barang()
        elif pilih == 5:
            find_barang()
        elif pilih == 6:
            sort_barang()
        elif pilih == 7:
            exit = input("keluar? (y/n): ")
            if exit == "y":
                break
        else:
            print("menu tidak tersedia!")

if __name__  == "__main__":
    main()