def bagi(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "angka tidak boleh 0"
    except TypeError:
        return "masukan angka yang benar"
    # finally:
    #     print("program selesai") menskip proses try dan except
    
print(bagi(8,"0"))
