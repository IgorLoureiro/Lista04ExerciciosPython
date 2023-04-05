print("Qual valor que cada um de vocês contribuiu para a loteria?")

Cont1 = int(input("Informe quanto foi a primeira contribuição?: \n"))
Cont2 = int(input("Informe quanto foi a segunda contribuição?: \n"))
Cont3 = int(input("Informe quanto foi a terceira contribuição? \n"))

Total = Cont1 + Cont2 + Cont3

PorcCont1 = Cont1/Total
PorcCont2 = Cont2/Total
PorcCont3 = Cont3/Total

Premio = 100000.00

Quantia1 = Premio * PorcCont1
Quantia2 = Premio * PorcCont2
Quantia3 = Premio * PorcCont3

print(f"A Quantia devida ao que contribuiu com R$ {Cont1} é de R${Quantia1: .2f}")
print(f"A Quantia devida ao que contribuiu com R$ {Cont2} é de R${Quantia2: .2f}")
print(f"A Quantia devida ao que contribuiu com R$ {Cont3} é de R${Quantia3: .2f}")