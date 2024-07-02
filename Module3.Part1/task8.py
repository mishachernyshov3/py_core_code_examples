# Гра в кидання кубика.
# Правила:
# Спочатку вводиться кількість гравців. Кожен гравець по черзі натискає [Enter] та бачить результати кидання кубика.
# Якщо в когось із гравців випало 2 і більше однакових чисел, перемагає той, в кого найбільше однакових чисел.
# Якщо таких гравців декілька, розпочинається наступний раунд за тима ж правилами.
import random
from collections import Counter


players_count = int(input("Enter the players count: "))
DICE_ROLLS_COUNT = 3

res = random.randint(1, 6)

players_results = []

for i in range(players_count):
    players_results.append([])


while True:
    players_results = []

    for player_index in range(players_count):
        input(f"Player {player_index + 1}, enter to roll dices: ")
        players_results.append([])

        for roll in range(DICE_ROLLS_COUNT):
            players_results[player_index].append(random.randint(1, 6))

        print(f"Player {player_index + 1} rolls: {players_results[player_index]}")

    players_duplications = []
    for player_index in range(players_count):
        counter = Counter(players_results[player_index])
        players_duplications.append(counter.most_common(1)[0][1])

    max_duplications_count = max(players_duplications)
    max_duplications_count_occurrences = Counter(players_duplications)[max_duplications_count]
    if max_duplications_count > 1 and max_duplications_count_occurrences == 1:
        winner_index = players_duplications.index(max_duplications_count)
        print(f"Player {winner_index + 1} is a winner")
        break
