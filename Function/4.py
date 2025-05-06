'''default fungsi argumen'''
# def fungsi(argument1 = "bla bla bla", argument2)
    # return
# fungsi(argument1 = "p", argument2 = 9)

# contoh 1
def pangkat(num1,num2):
    total = num1**num2
    return total
print(pangkat(num1 = 9, num2 = 2))

def sapa(sapa1,sapa2):
    print(f"halo namaku {sapa1}, adikku namanya {sapa2}")
    return sapa1,sapa2
print(sapa(sapa1 = "opik", sapa2 = "cika"))