def valor(valor):
    erro = 0
    for digito in valor:
        if valor.count(digito+digito) >= 1:
            erro += 1
            print('Número consecutivo')
            break
    soma = 0
    for digito in valor:
        soma += int(digito)
    if soma % 2 != 0:
        erro += 1
        print('Soma impar')
    if valor[0] == valor[-1]:
        erro += 1
        print('inicio fim igual')
    return erro

while True:
    valor1 = str(input(':'))
    print(valor(valor1))