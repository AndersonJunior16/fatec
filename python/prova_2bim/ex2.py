vet = []

n = int(input('Digite a quantidade numeros: '))

for i in range(n):
    vet.append(int(input(f"Digite o elemento {i+1} do vetor: ")))
    
X = int(input("Digite o valor de X: "))

contagem = vet.count(X)

print(f'O valor {X} aparece {contagem} dentro da lista ')