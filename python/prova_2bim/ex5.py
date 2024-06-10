vet = []
vet_neg = []
n = int(input('Digite a quantidade de numeros: '))

for i in range(n):
    vet.append(int(input(f'Digite o {i+1}° numero: ')))

for i in range(n):
    if vet[i] < 0:
        vet_neg.append(vet[i])

print(f'Na lista {vet} existem {len(vet_neg)} numeros negativos')
