vetor = [1, 2, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 9, 9, 10, 10, 11, 12, 12, 20]

for i in vetor:
    if vetor.count(i) > 1:
        vetor.remove(i)

print(vetor)