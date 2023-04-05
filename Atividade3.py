"""""
Soma = 0
Numero1 = int(input('Digite três numeros para serem somados: '))
Numero2 = int(input('Digite o segundo numero: '))
Numero3 = int(input('Digite o ultimo numero: '))

Soma = Numero1 + Numero2 + Numero3

print(Soma)

Numero = int(input('Quantas vezes você deseja adicionar? '))
Soma = 0

for n in range(1, Numero+1):
    num = int(input(f'Adicione {n}/{Numero} do valor a ser somado: '))
    Soma = Soma + num
print(f'O resultado da soma é {Soma}
"""


n1 = 1
soma = 0

while n1 < 4:
    numero = int(input(f'Adicione {n1}/3 do valor a ser somado: '))
    n1 = n1 + 1
    soma = soma + numero

print(f'O resultado da soma dos numeros resultou em: {soma}')
