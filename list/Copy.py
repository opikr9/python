# Copy menyalin data tanpa mengupdate data yang sudah dicopy
data = ["opak","opik","opek","opuk","opok"]
print(f"data asli sebelum : \n{data}\n")

noCopy = data
print(f"data tanpa copy sebelum : \n{noCopy}\n")

Copy = data
print(f"data copy sebelum : \n{Copy}\n")

# saat update data
noCopy[1] = "ubah"
print(f"data tanpa copy sesudah : \n{noCopy}\n ")

print(f"data asli sesudah : \n{data}\n")

noCopy = data.copy()
noCopy[1] = "tidak"
print(f"data tanpa copy sesudah : \n{noCopy}\n ")