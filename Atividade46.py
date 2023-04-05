Numero = int(input("Escreva um numero entre 100 e 999 para receber este de trás pra frente: \n"))

if Numero < 100 or Numero > 999:
    print("O Numero informado é superior ou inferior aos padrões solicitados")
else:
    Numero = str(Numero)
    print(Numero[::-1])
