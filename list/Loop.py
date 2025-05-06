# looping di list

# for loop
print("For Loop")
forCampur = [1,2,3,"a","i","u"]
for alphanum in forCampur:
    print(f"data For Loop : {alphanum}\n")

# for loop range
print("For Range Loop")
rangeCampur = ["machine","learning",1,2]
lenRange = len(rangeCampur)
for i in range(lenRange):
    print(f"data For Range Loop : {rangeCampur[i]}\n")

# while
print("While Loop")
whileCampur = [4,5,6,"e","o","p"]
lenWhile = len(whileCampur)
i = 0
while i < lenWhile:
    print(f"data While Loop : {whileCampur[i]}\n")
    i += 1

# List Compheresion
print("List Compheresion")
Comphr = [9,8,7,"p","y"]
[print(f"ini adalah list compheresion : {i}\n") for i in Comphr]

# enumerate mengambil data sekaligus index
enum = [11,22,33,"opik","cika","fira"]
for index,data in enumerate(enum):
    print(f"data enumerate. index : {index}, value : {data}")