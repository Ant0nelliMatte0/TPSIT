import random
def gen_mac():
    char_st = "ABCDEF0123456789"
    mac_addres = ""
    punti = 0
    for _ in range(6):
        for _ in range(2):
            mac_addres += random.choice(char_st)
        if punti < 5:
          mac_addres += ":"
          punti += 1
    return mac_addres