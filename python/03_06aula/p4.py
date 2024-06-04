n = int(input('Digite a quantidade de numeros reais: '))
vet = [''] * n
soma = 0

for i in range(n):
    n_reais = float(input(f'Digite {i+1}° numero: '))
    vet[i] = n_reais

for i in range(n):
    soma += vet[i]


print(f'A soma dos numeros é {round(soma,2)}')