from collections import deque

def play_cardgame(num_players, num_cards):
    card_sequence = deque([0])
    current_card = 0
    max_score = 0
    players_with_max_score = []

    if num_cards < 24:
        return max_score, players_with_max_score

    for i in range(1, num_cards, 23):
        if i % 23 != 0:
            prev_index = card_sequence.index(current_card)
            current_index = prev_index + 2
            if current_index > len(card_sequence):
                card_sequence.insert(1, i)
                current_card = i
            else:
                card_sequence.insert(current_index, i)
                current_card = i
        else:
            prev_index = card_sequence.index(current_card) - 7
            current_index = prev_index + 1
            player = i % num_players or num_players
            if player in players_with_max_score:
                players_with_max_score.remove(player)
            score = card_sequence[prev_index] + i
            if score > max_score:
                max_score = score
                players_with_max_score = [player]
            elif score == max_score:
                players_with_max_score.append(player)

            current_card = card_sequence[current_index]
            card_sequence.rotate(-prev_index)
            card_sequence.popleft()

    return max_score, players_with_max_score
