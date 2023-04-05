dia = int(input("Quantos dias você ira trabalhar como encanador? \n"))

GanhoBruto = dia * 30
GanhoLiquido = GanhoBruto - (GanhoBruto * 0.12)

print(f"Você ira receber como pagamento Bruto {GanhoBruto} Reais e após o desconto do INSS {GanhoLiquido} Reais ")