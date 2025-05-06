# count menghitung karakter di suatu var
dataStr = ["opik","cika","safira","opik","safira","opik"]
dataCount = dataStr.count("opik")
print(dataStr)
print(f"jumlah opik di data ada? : {dataCount}\n")

# mencari index dengan index["value"]
indexs = [9,"halo","hai","hehe",8]
dataIndexs = indexs.index("hehe")
print(indexs)
print(f"data hehe ada di index no : {dataIndexs}\n")

# sort untuk mengurutkan alpha dan num
sortStr = ["safira","opik","cika"]
print(f"sebelum : {sortStr}")
sortStr.sort()
print(f"sesudah : {sortStr}\n")

sortNum = [9,5,1,2]
print(f"sebelum : {sortNum}")
sortNum.sort()
print(f"sesudah : {sortNum}\n")

# reverse membalik
reverseStr = ["safira","opik","cika"]
print(f"sebelum : {reverseStr}")
reverseStr.reverse()
print(f"sesudah : {reverseStr}\n")

reverseNum = [9,5,1,2]
print(f"sebelum : {reverseNum}")
reverseNum.reverse()
print(f"sesudah : {reverseNum}\n")