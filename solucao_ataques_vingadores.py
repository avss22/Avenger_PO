from itertools import product

# Dados dos Vingadores
vingadores = [
    "Dr. Stephen Strange",
    "Iron Man",
    "Thor",
    "Captain America",
    "Black Widow",
    "Spider Man",
    "Star-Lord"
]

# Impacto gerado por um ataque de cada Vingador
impacto = [24, 21, 30, 13, 8, 18, 6]

# Limites de energia e gasto de energia por ataque
energia_disponivel = [250, 200, 300, 130, 90, 120, 50]
energia_por_ataque = [33, 21, 35, 13, 11, 18, 7]

# Tempo gasto por ataque, em segundos
tempo_por_ataque = [22, 20, 25, 10, 19, 24, 14]
tempo_maximo = 120

# Calcula o máximo de ataques de cada personagem considerando,
# simultaneamente, os limites de energia e de tempo.
limites = []
for i in range(len(vingadores)):
    limite_energia = energia_disponivel[i] // energia_por_ataque[i]
    limite_tempo = tempo_maximo // tempo_por_ataque[i]
    limites.append(min(limite_energia, limite_tempo))

melhor_impacto = -1
melhor_combinacao = None

# Avalia todas as combinações inteiras possíveis de ataques.
for combinacao in product(*[range(limite + 1) for limite in limites]):
    strange, iron_man, thor, capitao, viuva, spider_man, star_lord = combinacao

    # Restrições do enunciado
    if spider_man < 5:
        continue

    if thor > 6:
        continue

    if strange > 2 * iron_man:
        continue

    if capitao + viuva + iron_man + star_lord < thor + strange:
        continue

    # Calcula o impacto da combinação atual.
    impacto_total = sum(
        ataques * dano
        for ataques, dano in zip(combinacao, impacto)
    )

    # Armazena a combinação com o maior impacto encontrado.
    if impacto_total > melhor_impacto:
        melhor_impacto = impacto_total
        melhor_combinacao = combinacao

print("=" * 55)
print("SOLUÇÃO ÓTIMA: ATAQUES CONTRA THANOS")
print("=" * 55)

for nome, ataques, dano, energia, tempo in zip(
    vingadores,
    melhor_combinacao,
    impacto,
    energia_por_ataque,
    tempo_por_ataque
):
    print(f"{nome}: {ataques} ataque(s)")
    print(f"  Impacto: {ataques * dano}")
    print(f"  Energia usada: {ataques * energia}")
    print(f"  Tempo usado: {ataques * tempo} segundos")

print("=" * 55)
print(f"Impacto total máximo: {melhor_impacto} unidades")
print("=" * 55)
