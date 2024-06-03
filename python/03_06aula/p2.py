vet = []

n = int(input('Digite a quantidade de nomes: '))

for i in range(n):
    nomes = input(f'Digite {i+1}° nome: ')
    vet += [nomes]

print('Os elementos que se encontram nas posições impares são: ')
for i in range(n):
    if i % 2 == 1:
        print(f'Na posição {i} está o nome {vet[i]}')