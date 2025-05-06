# *args pada function
def fungsiNormal(nama,alamat,id):
    print(f"namaku {nama} aku tinggal di {alamat} dan anak ke-{id} ")

fungsiNormal("opik","pandansari",1)

def fungsiNormal(datalist):
    data = datalist.copy()
    nama = data[0]
    alamat = data[1]
    id = data[2]
    print(f"namaku {nama} aku tinggal di {alamat} dan anak ke-{id} ")
fungsiNormal(["cika","pandansari",2]) #perlu dijadikan list

def fungsiArgs(*args): #*args(bebas)
    nama = args[0]
    alamat = args[1]
    id = args[2]
    print(f"namaku {nama} aku tinggal di {alamat} dan anak ke-{id} ")
fungsiArgs("safira","pandansari","3")

def fungsiPangkat(*pangkat):
    output = int(input("masukan angka: "))
    for angka in pangkat:
        output **= angka
    
    return output
hasil = fungsiPangkat(2)
print(f"hasil : {hasil}")