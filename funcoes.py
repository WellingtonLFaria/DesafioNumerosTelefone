def gerar_numeros():
    numeros = []
    for c in range(0, 100):
        if c % 11 == 0:
            pass
        else:
            if c < 10:
                c = '0' + str(c)
            numeros.append(str(c))
    return numeros


def soma_strings(valores):
    numeros = []
    for valor in valores:
        for valor2 in valores:
            if valor[1] == valor2[0]:
                pass
            else:
                for valor3 in valores:
                    if valor2[1] == valor3[0] or valor[0] == valor3[1]:
                        pass
                    else:
                        caso = 0
                        for digito in valor+valor2+valor3:
                            if int(digito) % 2 != 0:
                                caso += 1
                        if caso == 1 or caso == 3 or caso == 5:
                            pass
                        else:
                            numeros.append(int(valor+valor2+valor3))
                            print(valor+valor2+valor3)
    return numeros

numeros = soma_strings(gerar_numeros())

print(numeros)
print(len(numeros))
