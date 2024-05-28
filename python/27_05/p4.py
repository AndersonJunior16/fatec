vet = []

n = int(input('Digite a quantidade de nomes: '))

for i in range(n):
    vet.append(input(f'Digite o {i+1}° nome: '))

for i in range(n):
        print(f'{vet[i]} tem {len(vet[i])} letras ')