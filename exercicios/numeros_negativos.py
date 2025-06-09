# Cria um vetor (lista) vazio
numeros = []

# Solicita 4 números ao usuário
for i in range(4):
    num = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

# Conta quantos números são negativos
negativos = 0
for num in numeros:
    if num < 0:
        negativos += 1

# Exibe o resultado
print(f"\nVocê digitou {negativos} número(s) negativo(s).")
