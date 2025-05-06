# menggunakan for dengan list
listFor = [x**2 for x in range(0,9)]
print(f"perhitungan dengan list for {listFor}\n")

# menghitung panjang dengan : len
listPanjang = len(["satu","dua","tiga"])
print(f"panjang list ini adalah : {listPanjang}\n")

# # ubah data list : []
listUpdate = ["opik","cika","safira"]
print(f"sebelum : {listUpdate}")

listUpdate[0] = ["sukses"]
print(f"sesudah : {listUpdate}\n")

# tambah data{bebas} : insert
Insert = ["machine","learning","deep","learning"]
print(f"sebelum : {Insert}")

Insert.insert(0,"Python")
print(f"sesudah : {Insert}\n")


# # tambah data{akhir} : append
Append = ["machine","learning","deep","learning"]
print(f"sebelum : {Append}")

Append.append("Python")
print(f"sebelum : {Append}\n")

# gabung data 1 dan 2 : extend
extend1 = ["random","salah"]
print(f"sebelum : {extend1}")

extend2 = ["random","benar"]
extend1.extend(extend2)
print(f"sesudah : {extend1}\n")

# hapus data{akhir} : pop
Pop = ["machine","learning","deep","learning"]
print(f"sebelum : {Pop}")

Pop.pop()
print(f"sebelum : {Pop}\n")

# hapus data{bebas} : remove
Remove = ["machine","learning","deep","learning"]
print(f"sebelum : {Remove}")

Remove.remove("learning")
print(f"sesudah : {Remove}\n")