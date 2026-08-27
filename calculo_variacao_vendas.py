vendas_2022 = float(input("Digite a quantidade de vendas em 2022: "))
vendas_2023 = float(input("Digite a quantidade de vendas em 2023: "))

# Passo 1: Calcular a variação percentual
# Fórmula: ((Valor de 2023 - Valor de 2022) / Valor de 2022) * 100
variacao = ((vendas_2023 - vendas_2022) / vendas_2022) * 100

print(f"Variação calculada: {variacao:.2f}%\n")

# Passo 2: A escada de decisões (if / elif / else)
if variacao > 20:
    print("Sugestão da diretoria: Bonificação para o time de vendas! 🚀")

elif variacao >= 2:
    print("Sugestão da diretoria: Pequena bonificação para o time de vendas. 👍")

elif variacao >= -10:
    print("Sugestão da diretoria: Planejamento de políticas de incentivo às vendas. 📈")

else:
    print("Sugestão da diretoria: Corte de gastos urgente. ⚠️")
