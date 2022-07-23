vetA = [int(i) for i in input().split(" ") if i]
vetB = [int(i) for i in input().split(" ") if i]

vetC = [0 for i in range(len(vetA) + len(vetB))]


contPar = 0
contImpar = 0


for c in range(0, len(vetC)):
    if(c % 2 == 0 or c == 0):
        vetC[c] = vetA[contPar]
        contPar += 1
    else:
        vetC[c] = vetB[contImpar]
        contImpar += 1

stringFinal = " ".join(map(str, vetC))
print(stringFinal)

