kontak = {}

# create
def tambah_kontak():
    nama = input("masukan nama kontak: ")
    if nama in kontak:
        print("nama kontak sudah terdaftar!")
        return
    nomor = int(input("masukan nomor kontak: "))
    email = input("masukan email kontak: ")
    desa = input("masukan desa: ")
    kecamatan = input("masukan kecamatan: ")
    
    kontak[nama] = {
        "nomor":nomor,
        "email":email,
        "alamat":{
            "desa":desa,
            "kecamatan":kecamatan
        }
    }
    tampilkan_kontak()
# read
def tampilkan_kontak():
    if not kontak:
        print("kontak belum tersedia")
    else:
        print("Daftar kontak")
        for kunci, isi in kontak.items():
            print(
                f"nama: {kunci}\nnomor: {isi['nomor']}\nemail: {isi['email']}\nalamat=> desa: {isi['alamat']['desa']} kecamatan: {isi['alamat']['kecamatan']}\n"
            )

def update_kontak():
    tampilkan_kontak()
    nama_lama = input("masukan nama kontak yang ingin diupdate: ")
    if nama_lama in kontak:
        nama_baru = input("masukan nama kontak baru: ")
        nomor_baru = int(input("masukan nomor kontak baru: "))
        email_baru = input("masukan email kontak baru: ")
        desa_baru = input("masukan desa baru: ")
        kecamatan_baru = input("masukan kecamatan baru: ")

        kontak[nama_baru] = {
        "nomor":nomor_baru,
        "email":email_baru,
        "alamat":{
            "desa":desa_baru,
            "kecamatan":kecamatan_baru
            }
        }
        if nama_lama != nama_baru:
            del kontak[nama_lama]

            print(f"kontak berhasil diupdate {nama_baru}")
    else:
        print("kontak tidak ditemukan")

def hapus_kontak():
    tampilkan_kontak()
    del_kontak = input("masukan nama kontak yang ingin dihapus: ")
    if del_kontak in kontak:
        conf = input(f"hapus {del_kontak}? (y/n): ")
        if conf == "y":
            kontak.pop(del_kontak)
    else:
        print("kontak tidak tersedia!")

def cari_kontak():
    find_nama = input("masukan nama kontak yang ada cari: ")
    if find_nama in kontak:
        print(f"{find_nama}: {kontak[find_nama]}")
    else:
        print("kontak tidak ditemukan!")

def cari_email():
    find_email = input("masukan nama email kontak yang ada cari: ")
    ketemu = False
    for kunci, isi in kontak.items():
        if isi['email'] == find_email:
            print("kontak ditemukan")
            print(
                f"nama: {kunci}\nnomor: {isi['nomor']}\nemail: {isi['email']}\nalamat=> desa: {isi['alamat']['desa']} kecamatan: {isi['alamat']['kecamatan']}\n"
            )
            ketemu = True
            break
        else:
            print("kontak tidak ditemukan!")




def main():
    while True:
        print("\n1. Tambah kontak")
        print("2. Tampilkan kontak")
        print("3. Update kontak")
        print("4. Hapus kontak")
        print("5. Cari kontak")
        print("6. Cari email")
        print("7. exit")

        pilih = int(input("masukan pilihan: "))

        if pilih == 1:
            tambah_kontak()
        elif pilih == 2:
            tampilkan_kontak()
        elif pilih == 3:
            update_kontak()
        elif pilih == 4:
            hapus_kontak()
        elif pilih == 5:
            cari_kontak()
        elif pilih == 6:
            cari_email()
        elif pilih == 7:
            exit = input("keluar? (y/n): ")
            if exit == "y":
                break
        else:
            print("menu tidak tersedia!")

if __name__  == "__main__":
    main()