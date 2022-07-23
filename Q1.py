def removeVogais(string):
    strNew = ""
    for c in range(0, len(string)):
        strLow = string.lower()
        if(strLow[c] != "a" and strLow[c] != "e" and strLow[c] != "i" and strLow[c] != "o" and strLow[c] != "u"):
            strNew += "{}".format(string[c])
    return strNew + "7VXDVt"


texto = str(input())

print(removeVogais(texto))


