vet = []
vet_cont =[]

n = int(input('Digite a quantidade numeros: '))

for i in range(n):
    vet.append(int(input(f"Digite o elemento {i+1} do vetor: ")))

for i in range(n):
    if vet[i] > vet[i-1] and vet[i] != vet[0] and vet[i] != vet[-1]:
        vet_cont.append(vet[i])

print(f'A lista contigua é {vet_cont}')