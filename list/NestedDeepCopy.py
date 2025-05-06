data1 = [1,2]
data2 = [3,4]
data = [data1,data2,9]
data_copy = data.copy()
print(f"isi data : {data}")
print(f"isi data copy : {data_copy}")

print(f"data index 0,1: {data[0][1]}")
print(f"data copy index 0,1: {data[0][1]}\n")

# cek hex id masing2 data sekilas berbeda tapi isinya sama
print(f"id data : {hex(id(data))}")
print(f"id data copy : {hex(id(data_copy))}\n")

#cek hex id isinya sama
print(f"id data index 0,1: {hex(id(data[0][1]))}")
print(f"id data copy index 0,1: {hex(id(data_copy[0][1]))}\n")

# diperlukan deepcopy untuk mengcopy sampai dalam efeknya deepcopy tidak ikut berubah sama update
from copy import deepcopy
data_deepcopy = deepcopy(data)

# cek dengan update
data[0][1] = 10
print(f"data: {data}")
print(f"data copy : {data_copy}")
print(f"data deepcopy: {data_deepcopy}\n")

print(f"id data index 0,1: {hex(id(data[0][1]))}")
print(f"id data copy index 0,1: {hex(id(data_copy[0][1]))}")
print(f"id data deepcopy index 0,1: {hex(id(data_deepcopy[0][1]))}")