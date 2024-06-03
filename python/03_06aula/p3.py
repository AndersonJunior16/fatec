n = int(input('Digite a quantidade de nomes: '))
vet = [''] * n


for i in range(n):
    nomes = input(f'Digite {i+1}° nome: ')
    vet[i] = nomes

for i in range(n):
    if len(vet[i]) > 5:
        print(f'{vet[i]} tem mais de 5 letras')