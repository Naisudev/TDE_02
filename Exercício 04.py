vetor = []

for i in range(1, 7):
    vetor.append(int(input('Digite um número inteiro: ')))
    if i >= 6:
        vetor.reverse()
        print(vetor)
