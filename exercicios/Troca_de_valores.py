#solicita ao usuário os dois valores
valor1 = input("Digite um valor:")
valor2 = input("Digite um valor:")

# Exibe os valores antes da troca
print("/nAntes da troca:")
print("valor 1:", valor1)
print("valor 2:", valor2)

#Troca os valores
valor1, valor2 = valor2, valor1

# Exibe os valores após a troca
print("/nDepois da troca:")
print("valor 1:", valor1)
print("valor 2:", valor2)