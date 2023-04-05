salariobase = int(input("Qual seu salário base? \n"))

gratificacao = salariobase * 0.05

desconto = salariobase * 0.07

print(f"Você recebe {gratificacao: .2f} Reais de Gratificação e paga {desconto: .2f} Reais de desconto, resultando em "
      f" um salário líquido de {salariobase - desconto + gratificacao: .2f} Reais")