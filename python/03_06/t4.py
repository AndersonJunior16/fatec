vetA = []
vetB = []
vetC = []

n = int(input('Digite a quantidade de números: '))

for i in range(n):
    numeroA = int(input(f'Digite {i+1}º número de A: '))
    numeroB = int(input(f'Digite {i+1}º número de B: '))
    vetA.append(numeroA)
    vetB.append(numeroB)
    if numeroA == numeroB:
        vetC.append(numeroA)

print(f'Os numeros de A são: {vetA}')
print(f'Os numeros de B são: {vetB}')
print(f'Os numeros iguais são: {vetC}')