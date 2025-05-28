def contar_numeros_negativos():

  vetor = []
  cont = 0

  print("Digite 4 números:")
  for i in range(4):
    num = float(input(f"Número {i+1}: "))  # Leitura de números com ponto flutuante
    vetor.append(num)

  for num in vetor:
    if num < 0:
      cont += 1

  print(f"A quantidade de números negativos digitados foi: {cont}")


# Chamada da função
contar_numeros_negativos()