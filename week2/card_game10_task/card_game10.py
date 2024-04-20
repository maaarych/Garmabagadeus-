from timeit import default_timer as timer

# START MY TIMER
from collections import deque

def play_cardgame(num_players, num_cards):
    base = deque([0])
    main = 0
    max = 0, set()
    dict_ = {}

    if num_cards < 24:
        return max

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
            if player in dict_:
                dict_[player] += base[ind_prev] + i
            else:
                dict_[player] = base[ind_prev] + i
            if dict_[player] > max[0]:
                max = dict_[player], set([player])

            main = base[ind_cur]
            base.rotate(-ind_prev)
            base.popleft()

    return max

