vet = []

n = int(input('Digite a quantidade de numeros: '))

for i in range(n):
    vet.append(int(input(f'Digite {i+1}° numero: ')))

for i in range(n):
    print(f'elemento {vet[i]} na posição {i}')