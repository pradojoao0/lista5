
vetorB = "63";
vetorA = str(input()).split(" ")

contador = 0

for c in range(0, len(vetorA)):
    if(vetorB in vetorA[c]):
        contador += 1
print("O texto 63 ocorre {} vez(es) na entrada lida.".format(63))
