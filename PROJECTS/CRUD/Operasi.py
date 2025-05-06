from . import Database
from .Util import random_string
import time
import os

def delete(no_buku):
    print(no_buku)
    try:
        with open(Database.DB_NAME,'r') as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku -1:
                    pass
                else:
                    with open("recycle.txt","a",encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")

    os.rename("recycle.txt",Database.DB_NAME)
    



def update(no_buku,pk,date_add,judul,penulis,tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with open(Database.DB_NAME,"r+",encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)

    except:
        print("erorr update data")

def create(judul,penulis,tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,"a",encoding="utf-8") as file:
            file.write(data_str)
            print("data berhasil ditambahkan!")
    except:
        print("gagal menambahkan data")
def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    tahun = input("Tahun: ")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("gagal menambahkan data")

def read(**kwargs):
    try:
        with open(Database.DB_NAME,"r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("Gagal membaca data!")
        return False