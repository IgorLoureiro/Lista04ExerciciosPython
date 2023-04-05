"""""
leia quatro notas, cálcule a média aritmética e imprima o resultado

"""""

Soma = 0
n1 = 1

while n1 < 5:
    Numero = int(input(f'Adicione {n1}/4 do valor para cálcular a média aritmética destes \n'))
    n1 = n1 + 1
    Soma = Soma + Numero
print(f'A média aritmética dos numeros informados é igual a {Soma/4}')