"""
Leia um numero inteiro e imprima a soma do sucessor do seu triplo (Numero*3+1) e o antecessor de seu dobro (Numero*2-1)
"""

Numero = int(input('Digite um número \n'))

Numero1 = (Numero * 3) + 1

Numero2 = (Numero * 2) - 1

print(f'A soma do sucessor do triplo {Numero1} com o antecessor de seu dobro {Numero2} é igual a {Numero1 + Numero2}')

