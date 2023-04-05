Numeros = []

for n in range(1, 3):
    SolicitarNum = int(input('Informe A e B para cálcular a hipotenusa: \n'))
    Numeros.append(SolicitarNum)

Num1, Num2 = Numeros

print(Num1)
print(Num2)

Hipotenusa = ((Num1**2) + (Num2**2))**(1/2)

print(Hipotenusa)

