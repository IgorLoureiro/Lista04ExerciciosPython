Numero = int(input("Digite um numero entre 1000 e 9999 para receber um digito por linha: \n"))

if Numero < 1000 or Numero > 9999:
    print("O numero informado não se encaixa nos padrões solcitados")
else:
    Numero = str(Numero)

    print(Numero[0])
    print(Numero[1])
    print(Numero[2])
    print(Numero[3])
