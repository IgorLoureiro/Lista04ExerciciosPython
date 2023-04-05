Letra = input("Informe a letra maiuscula que deseja converter para minuscula: \n")

LetraOrd= ord(Letra)
LetraMinusculaOrd = LetraOrd + 32
LetraMinuscula= chr(LetraMinusculaOrd)

print(LetraMinuscula)