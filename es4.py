def Cod(cifrari, stringa)
strSucc= ""
for car in stringa:
    if car in cifrario:
        strSucc += cifrario[car]
    else:
        strSucc += car
print("Rot-15")
print(strSucc)

def main():
    cifrario = {'a': 'p', 'b': 'q', 'c': 'r', 'd': 's', 'e': 't', 'f': 'u',
                'g': 'v', 'h': 'w', 'i': 'x', 'j': 'y', 'k': 'z', 
                'l': 'a', 'm': 'b', 'n': 'c', 'o': 'd', 'p': 'e', 'q': 'f', 
                'r': 'g', 's': 'h', 't': 'i', 'u': 'j', 'v': 'k', 
                'w': 'l', 'x': 'm', 'y': 'n', 'z': 'o'}
    stringa= input("inserire una stringa a piacere")
    Cod(cifrario, stringa)
if __name__ == "__main__":
    main()