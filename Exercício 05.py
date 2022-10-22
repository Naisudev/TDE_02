vetor = [8, 2, 3, 2, 5, 5, 7, 8, 9, 10]

vetorIguais = []

for i in vetor:
    if vetor.count(i) > 1:
        vetorIguais.append(i)

print(vetorIguais)