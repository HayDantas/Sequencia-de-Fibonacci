def verificacao_fibonacci(n):
    a,b = 0, 1
    while b < n :
        a, b = b , a + b 
    if b == n:
        return True
    else: 
        return False


numero = int (input("Digite um numero: "))
sequencia_fibonacci = [0,1]

while sequencia_fibonacci [-1] < numero: 
    sequencia_fibonacci.append(sequencia_fibonacci[-1] + sequencia_fibonacci[-2])

if numero in sequencia_fibonacci:
    print (f"{numero} faz parte da sequencia de fibonacci")
else:
    print(f"{numero} não faz parte da sequencia de fibonacci")
 
     
