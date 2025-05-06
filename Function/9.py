# lambda function operasi 1
pikFnc = lambda num : num**2

print(f"hasil lambda fnc1: {pikFnc(9)}\n")

# lambda function operasi 2
pikFnc = lambda num,pow : num**pow

print(f"hasil lambda fnc2: {pikFnc(3,9)}")

# untuk kebutuhan list
dataFind = [9,3,5,6,1,5,6]

finds = list(filter(lambda x : x<7,dataFind))
print(finds)

aGanjil = [2,6,7,2,9,3,5,4,7,1]

Ganjil = list(filter(lambda x : (x%2==1),aGanjil))
print(Ganjil)

aGenap = [2,6,7,2,9,3,5,4,7,1]

Genap = list(filter(lambda x : (x%2==0),aGenap))
print(Genap)

dataSort = ["opik","safira","cika"]

#dataSort.sort(key=lambda nama:len(nama)) menghitung panjang
dataSort.sort(key=lambda nama:nama.lower())
print(dataSort)

# anonnymous function
def bagi(x):
    return lambda angka:angka/x

hasilBagi = bagi(3)
print(f"hasil bagi anonymous function: {hasilBagi(27)}")

def pangkat(y):
    return lambda nums:nums**y
print(f"hasil pangkat anonymous function: {pangkat(4)(5)}") #ini 5^4