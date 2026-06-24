# Recebe a temperatura corporal do paciente como entrada
entrada = input()

# Converte a entrada para float para permitir comparação decimal
temperatura = float(entrada)

if temperatura >= 37.5:
    print("Atendimento imediato")
else:
    print("Aguardar")

# TODO: Implemente a decisão condicional para imprimir "Atendimento imediato" se a temperatura for maior ou igual a 37.5, ou "Aguardar" caso contrário.
