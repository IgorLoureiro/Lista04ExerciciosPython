Premio = 780000.00

PrimeiroLugar = Premio * 0.46

SegundoLugar = Premio * 0.36

TerceiroLugar= Premio * (1 - (0.46 + 0.36))

print(f"O primeiro lugar ganhou {PrimeiroLugar: .2f}")
print(f"O segundo lugar ganhou {SegundoLugar: .2f}")
print(f"O terceiro lugar ganhou {TerceiroLugar: .2f}")

