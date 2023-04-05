print(f"Informe as horas, os minutos e os segundos atuais, bem como a duração do evento ao qual você ira participar "
"para receber o horário de termino do evento")

Hora = int(input("Informe a Hora: "))
Minuto = int(input("Informe os minutos: "))
Segundos = int(input("Informe os segundos: "))
Duracao = int(input("Informe a duração do evento em segundos: "))

HoraS = Hora*3600
MinutoS= Minuto*60

TerminoSeg = HoraS + MinutoS + Segundos + Duracao

HoraFinal = TerminoSeg/3600
MinutoFinal = (TerminoSeg%3600)/60
SegundoFinal = (TerminoSeg%3600)%60

print(f"o Horário de término do evento é de {HoraFinal: .0f} Horas, {MinutoFinal: .0f} Minutos e {SegundoFinal: .0f} "
      f"Segundos")