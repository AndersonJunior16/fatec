vet = []
pares = []

n = int(input('Digite a quantidade de números: '))

for i in range(n):
    numero = int(input(f'Digite {i+1}º número: '))
    vet.append(numero)
    if numero % 2 == 0:
        pares.append(numero)

print('Os elementos pares são: ')
print(pares)