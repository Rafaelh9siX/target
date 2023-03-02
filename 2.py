numero = int(input("Digite o numero para procurar "))
ultimo=1
penultimo=1

proximo = 0
while numero > proximo:
    proximo = ultimo + penultimo
    penultimo = ultimo
    ultimo = proximo

if numero == proximo:
    print("O numero faz parte da  sequência de Fibonacci")
else:
    print("O numero não faz parte da  sequência de Fibonacci")