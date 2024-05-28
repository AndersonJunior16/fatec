vet = []

n = int(input('Digite a quantidade de numeros: '))

for i in range(n):
    vet.append(int(input(f'Digite {i+1}° numero: ')))

print('Os elementos que se encontram nas posições pares são: ')
for i in range(n):
    if i % 2 == 0:
        print(f'{vet[i]} na posição {i}')