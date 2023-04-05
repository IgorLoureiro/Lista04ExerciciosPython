import math

Degrau = int(input("Qual o tamanho de cada degrau? \n"))

Altura = int(input("Até que altura você deseja subir? \n"))

QuantidadeDegrau = math.ceil(Altura/Degrau)

print(f"Você ira precisar subir {QuantidadeDegrau} Degraus")