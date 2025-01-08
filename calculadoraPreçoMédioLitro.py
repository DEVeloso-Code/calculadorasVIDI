# Solicita ao usuário a quantidade de bebida em ml
quantidade_ml = float(input("Digite a quantidade da bebida em ml: "))

# Solicita ao usuário o preço médio da bebida
preco_medio = float(input("Digite o preço médio da bebida: "))

# Calcula o preço por litro
preco_por_litro = (preco_medio / quantidade_ml) * 1000

# Exibe o resultado
print(f"O preço por litro é: R${preco_por_litro:.2f}")
