def calcular_dias_de_vividos (idade) :
  dias = idade * 365
  return dias

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

dias_de_vida = calcular_dias_de_vividos(idade)

print(f"olá {nome} você já viveu {dias_de_vida} dias")