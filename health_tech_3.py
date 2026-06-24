# Recebe o sintoma informado pelo paciente
sintoma = input().strip()  # Remove espaços extras

if sintoma == "dor no peito" or sintoma == "falta de ar":
    print("atendimento imediato")

elif sintoma == "febre" or sintoma == "tosse":
    print("agendar consulta")
else:
    print("repouso em casa")
# TODO: Implemente a estrutura condicional para decidir a orientação correta
# Dica: Use if/elif/else para comparar o sintoma com as opções do enunciado
# Exemplo de saída: print("atendimento imediato"), print("agendar consulta") ou print("repouso em casa")
