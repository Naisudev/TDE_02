import random

vetor = []

for i in range(1, 51):
    vetor.append(random.randint(0, 20))
    if i >= 50:
        print(vetor)

# a)
soma = sum(vetor)
print(soma)

# b)
contagem = vetor.count(9)
print(contagem)

# c)
maiorNum = max(vetor)
print (maiorNum)

# d)
menorNum = min(vetor)
print(menorNum)