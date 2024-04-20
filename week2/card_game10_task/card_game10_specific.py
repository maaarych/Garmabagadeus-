from timeit import default_timer as timer
from collections import deque

def play_card_game(num_players, num_cards):
    base = deque([0])
    main = 0
    max_score = 0
    max_players = set()
    player_scores = {}

    if num_cards < 24:
        return max_score, max_players

    for i in range(1, num_cards):
        if i % 23 != 0:
            ind_prev = base.index(main)
            ind_cur = ind_prev + 2
            if ind_cur > len(base):
                base.insert(1, i)
                main = i
            else:
                base.insert(ind_cur, i)
                main = i
        else:
            ind_prev = base.index(main) - 7
            ind_cur = ind_prev + 1
            player = i % num_players or num_players
            player_scores[player] = player_scores.get(player, 0) + base[ind_prev] + i
            if player_scores[player] > max_score:
                max_score = player_scores[player]
                max_players = {player}

            main = base[ind_cur]
            base.rotate(-ind_prev)
            base.popleft()

    return max_score, max_players
