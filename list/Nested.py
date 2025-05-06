# List Bersarang Tidak Berpengaruh di copy harus pakai nested copy
sarang1 = ["string1","string2","string3"]
sarang2 = [1,2,3]
bersarang = [sarang1,sarang2]
bersarang2 = [sarang1,sarang2,bersarang,"ini","list","bersarang",1]
print(f"list sarang 1 : {sarang1}\n")
print(f"list sarang 2 : {sarang2}\n")
print(f"list bersarang : {bersarang}\n")
print(f"list bersarang2 : {bersarang2}")