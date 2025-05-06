# **kwargs function

def fungsiNormal(nama,alamat,id):
    print(f"namaku {nama} aku tinggal di {alamat} dan anak ke-{id} ")

fungsiNormal("opik","pandansari",1)

def fungsiKwargs(**kwargs):
    nama = kwargs["nama"]
    alamat = kwargs["alamat"]
    id = kwargs["id"]

    print(f"namaku {nama} aku tinggal di {alamat} dan anak ke-{id}\n")

fungsiKwargs(nama="cika",alamat="pandansari",id=2)

def fungsiKwargsArgs(*args,**kwargs):
    if kwargs["option"] == "tambah":
        output = 0
        for angka in args:
            output += angka
        print(f"hasil output pertambahan = {output}\n")
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
        print(f"hasil output perkalian = {output}\n")
    else:
        print("tidak ada hasil")
    return output

hasil = fungsiKwargsArgs(1,2,3,option="tambah")
hasil = fungsiKwargsArgs(1,2,3,4,option="kali")