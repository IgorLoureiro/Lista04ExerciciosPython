"""""
Leia três valores, cálcule a raiz quadrada de cada um e apresente a soma delas
"""""
import math

Soma = 0

for n in range(1, 5):
    numero = int(input(f'Adicione {n}/4 do valor a ser somado sua raiz quadrada \n'))
    Soma = Soma + math.sqrt(numero)

print(f'A soma dos quadrados dos numeros informados é igual a {Soma}')