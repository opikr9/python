# function hints

'''def fungsiNormal(argument):
    panggil = argument
    return panggil
pemanggilan = fungsiNormal(argument="ini fungsi normal")
print(pemanggilan)'''

# import string
# def fungsiHintsString(argument = string) -> string:
#     panggil = argument

#     return panggil
# pemanggilan = fungsiHintsString(1)
# print(pemanggilan)

def fungsiHintsInt(argument:int) -> int:
    panggil = argument+1

    return panggil
PANGGILAN = fungsiHintsInt(1) #("hola")
print(PANGGILAN)