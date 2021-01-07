import random
import string
def gen_psw():
    print("scegli il livello di complessità della password che verrà generata")
    ascii_chars = string.digits + string.ascii_letters + string.punctuation
    alphanum_chars = string.digits + string.ascii_letters
    if input("scegi una password semplice o difficile? S/D ") == "S":
        lung = 8
        tipo = alphanum_chars
    else:
        lung = 20
        tipo = ascii_chars
    psw = ""
    cont = 0
    while cont < lung:
        char = random.choice(tipo)
        psw += char
        cont += 1
    print(f"La password generata è: {psw}")