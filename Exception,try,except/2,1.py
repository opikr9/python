from numbers import Number

def inputUser(x,y):
    if not isinstance(x,Number) or not isinstance(y,Number):
        raise f"input harus angka"
    return x+y
hasil = inputUser(8,9)
print(f"hasil inputUser: {hasil}")

angka = 0

try:
    hasil = 10/angka
except Exception as message_error:
    print(message_error)

except ZeroDivisionError as message_error:
    print(message_error)