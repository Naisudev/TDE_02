vetor1 = [0, 2, 11, 22, 5, 78, 0, 55, 14, 0, 0, 30, 66, 0, 15]

vetor2 = []

for i in vetor1:
    if i > 0:
        vetor2.append(i)

quantZeros = (len(vetor1) - len(vetor2)) * [0]

vetor2 = vetor2 + quantZeros

print(vetor2)