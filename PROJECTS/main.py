import os
import CRUD as CRUD

if __name__ == "__main__":
    osSystem = os.name
    match osSystem:
        case "posix":os.system("clear")
        case "nt":os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================\n")

    CRUD.init_console()

while(True):
    match osSystem:
        case "posix":os.system("clear")
        case "nt":os.system("cls")
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================\n")

    print("1. READ BOOK")
    print("2. INSERT BOOK")
    print("3. UPDATE BOOK")
    print("4. REMOVE BOOK")

    input_user = int(input("masukan pilihan: "))

    match input_user:
        case 1: CRUD.read_console()
        case 2: CRUD.create_console()
        case 3: CRUD.update_console()
        case 4: CRUD.delete_console()

    lagi = input("lanjut? (y/n): ")
    if lagi == 'n':
        break
print("Akhir Program")