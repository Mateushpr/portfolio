
valor_original = float(input("Digite o valor do produto: R$ "))


if valor_original > 100:
    desconto = valor_original * 0.10  
    valor_com_desconto = valor_original - desconto
    print(f"O valor com desconto de 10% é: R$ {valor_com_desconto:.2f}")
else:
    print("O valor não é suficiente para obter desconto.")
