vetor = []

num = 0

numPar = 0

numImpar = 0

maiorCinco = 0

while num > -1:
    num = int(input("Digite um número: "))
    if num > -1:
        vetor.append(num)
        if num > 5:
            maiorCinco = maiorCinco + 1
        if num % 2 == 0:
            numPar = numPar + num
        else:
            numImpar = numImpar + num

# a)
print(vetor)

# b)
print(maiorCinco)

# c)
print(numPar)

# d)
print(numImpar)

# e)
quantidade = len(vetor)
print(quantidade)
