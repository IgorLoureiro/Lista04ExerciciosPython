Segundos = int(input("Informe os segundos para transformar em minutos: \n"))

Horas = Segundos//3600

DiferencaMinutos = Segundos % 3600
Minutos = DiferencaMinutos//60

Segundo = DiferencaMinutos % 60


print(f"Os segundos informados são iguais a {Horas} Horas {Minutos} Minutos e {Segundo} Segundos")