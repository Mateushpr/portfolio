idade = int(input("Digite a sua idade:"))

if idade < 10:
    print("Você é criança!")

elif idade >= 10 and idade < 18 :
    print("Você é adolescente!")

elif idade >= 18 and idade < 24 :
    print("Você é um jovem adulto!")

elif idade > 24 :
    print("Você é um adulto!")

else:
    print("digite um valor válido!")
