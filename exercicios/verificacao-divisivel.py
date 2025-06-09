# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Verifica se é divisível por 3 e por 5 ao mesmo tempo
if numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 3 e por 5 ao mesmo tempo.")
else:
    print("O número NÃO é divisível por 3 e por 5 ao mesmo tempo.")
