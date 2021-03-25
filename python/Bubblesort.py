#Bubble sort.
array = []
numeroEle = int(input("Inserire il numero di elementi: "))
c = 0
print(f"Inserire {numeroEle} valori.")
while(c< numeroEle):
        inputValore = int(input("Inserire il valore valore: "))      
        array.append(inputValore)
        c = c + 1
c = 0
c2 = 0
for n in range(numeroEle - 1):
        for c2 in range(numeroEle- c - 1):	
                if(array[c2]>array[c2+1]):
                        swap = array[c2]
                        array[c2] = array[c+1]
                        array[c+1] = swap
print("Operazione completata con successo:")
print(array)
