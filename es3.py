def sequenza_Fibonacci(n):
    if n <= 1:
        return n
    else:
        return sequenza_Fibonacci(n-1) + sequenza_Fibonacci(n-2)
lim = int(input("Inserisci il numeo di elementi che si vogliono visualizzare nella serie di Fibonacci: "))
for num in range(1, lim+1):
    print(sequenza_Fibonacci(num))