sintoma = input().strip()

if sintoma == "dor no peito" or sintoma == "falta de ar":
    print("atendimento imediato")

elif sintoma == "febre" or sintoma == "tosse":
    print("agendar consulta")
else:
    print("repouso em casa")
