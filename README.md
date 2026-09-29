# Avenger_PO
from itertools import product

# Lista com os nomes dos Vingadores participantes
vingadores = [
    "Dr. Stephen Strange",
    "Iron Man",
    "Thor",
    "Captain America",
    "Black Widow",
    "Spider Man",
    "Star-Lord"
]

# Impacto produzido por um ataque de cada personagem
impacto = [24, 21, 30, 13, 8, 18, 6]

# Energia máxima disponível para cada personagem
energia_disponivel = [250, 200, 300, 130, 90, 120, 50]

# Energia gasta em cada ataque
energia_por_ataque = [33, 21, 35, 13, 11, 18, 7]

# Tempo gasto em segundos por ataque
tempo_por_ataque = [22, 20, 25, 10, 19, 24, 14]

# Dois minutos = 120 segundos
tempo_maximo = 120

# Descobre o máximo de ataques permitido para cada Vingador,
# considerando ao mesmo tempo a energia e o tempo.
limites = []

for i in range(len(vingadores)):
    limite_energia = energia_disponivel[i] // energia_por_ataque[i]
    limite_tempo = tempo_maximo // tempo_por_ataque[i]

    limites.append(min(limite_energia, limite_tempo))

# Variáveis para armazenar a melhor solução encontrada
melhor_impacto = -1
melhor_combinacao = None

# Testa todas as possibilidades de quantidade de ataques
for combinacao in product(
    range(limites[0] + 1),
    range(limites[1] + 1),
    range(limites[2] + 1),
    range(limites[3] + 1),
    range(limites[4] + 1),
    range(limites[5] + 1),
    range(limites[6] + 1)
):
    strange, iron_man, thor, capitao, viuva, spider_man, star_lord = combinacao

    # Regra 1: Spider Man deve atacar pelo menos 5 vezes
    if spider_man < 5:
        continue

    # Regra 2: Thor pode atacar no máximo 6 vezes
    if thor > 6:
        continue

    # Regra 3: Strange não pode atacar mais que o dobro do Iron Man
    if strange > 2 * iron_man:
        continue

    # Regra 4: ataques de Capitão, Viúva, Iron Man e Star-Lord
    # devem ser pelo menos iguais aos ataques de Thor e Strange
    if capitao + viuva + iron_man + star_lord < thor + strange:
        continue

    # Calcula o impacto total da combinação atual
    impacto_total = sum(
        combinacao[i] * impacto[i]
        for i in range(len(vingadores))
    )

    # Atualiza a melhor solução caso o impacto seja maior
    if impacto_total > melhor_impacto:
        melhor_impacto = impacto_total
        melhor_combinacao = combinacao

# Mostra o resultado
print("Melhor combinação de ataques:\n")

for i in range(len(vingadores)):
    print(f"{vingadores[i]}: {melhor_combinacao[i]} ataque(s)")

print(f"\nImpacto total máximo: {melhor_impacto} unidades")
