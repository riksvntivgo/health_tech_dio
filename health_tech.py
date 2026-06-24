# Lê a temperatura corporal informada pelo paciente
entrada = input()
temperatura = float(entrada)  # Converte a entrada para decimal

if temperatura < 36.0:
    print("Hypothermia")
elif temperatura >= 36.0 and temperatura <= 37.5:
    print("Normal")
else:
    print("Fever")


# TODO: Implemente a estrutura condicional para classificar a temperatura
# Dica: Use if, elif e else para verificar as faixas e imprimir "Hypothermia", "Normal" ou "Fever"