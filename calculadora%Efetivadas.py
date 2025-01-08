# Solicita o número total de visitas realizadas
total_visitas = int(input("Digite o número total de visitas realizadas: "))

# Solicita o número de visitas efetivadas
visitas_efetivadas = int(input("Digite o número de visitas efetivadas: "))

# Solicita o número de visitas não efetivadas
visitas_nao_efetivadas = int(input("Digite o número de visitas não efetivadas: "))

# Calcula as porcentagens
percentual_efetivadas = (visitas_efetivadas / total_visitas) * 100
percentual_nao_efetivadas = (visitas_nao_efetivadas / total_visitas) * 100

# Exibe os resultados
print(f"Porcentagem de visitas efetivadas: {percentual_efetivadas:.2f}%")
print(f"Porcentagem de visitas não efetivadas: {percentual_nao_efetivadas:.2f}%")
