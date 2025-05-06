from . import Operasi


def delete_console():
    read_console()
    while(True):
        print("Masukan no buku yang akan di update")
        no_buku = int(input("No Buku: "))
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            print(f"1. Judul\t: {judul:.40}")
            print(f"2. penulis\t: {penulis:.40}")
            print(f"3. tahun\t: {tahun:4}")
            Done = input("Selesai Hapus? (y/n): ")
            if Done == 'y':
                Operasi.delete(no_buku)
                break
        else:
            print("nomor buku tidak ditemukan")
    print("data berhasil dihapus")

def update_console():
    read_console()
    while(True):
        print("Masukan no buku yang akan di update")
        no_buku = int(input("No Buku: "))
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]
            break
        else:
            print("nomor buku tidak ditemukan")
    

    while(True):
        # data yang ingin diubah
        print("="*100+"\n")
        print("Masukan data yang ingin diubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. penulis\t: {penulis:.40}")
        print(f"3. tahun\t: {tahun:4}")

        input_user = input("Masukan Pilihan [1,2,3]: ")

        match input_user:
            # memilih mode update
            case "1": judul = input("judul\t: ")
            case "2": penulis = input("penulis\t: ")
            case "3": 
                while(True):
                    try:
                        tahun = int(input("Tahun: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Harap masukan 4 angka tanpa inputan lain!")    
                    except:
                        print("Harap masukan 4 angka tanpa inputan lain!")
            case _: print("tidak ada index")
        Done = input("Selesai Update? (y/n): ")
        if Done == 'y':
            break

        Operasi.update(no_buku,pk,date_add,judul,penulis,tahun)

def create_console():
    judul = input("Judul: ")
    penulis = input("penulis: ")
    while(True):
        try:
            tahun = input("tahun: ")
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus 4 angka")
        except:
            print("tahun harus 4 angka") 

    Operasi.create(judul,penulis,tahun)
    print("berikut adalah data anda")
    read_console()


def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # header
    print("="*100+"\n")
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100+"\n")

    # data
    for index,data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]

        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")

    # footer
    print("="*100+"\n")