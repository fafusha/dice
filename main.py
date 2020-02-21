import random as rnd

roll_dice = lambda n: {rnd.randrange(1, 7) for i in range(n)}

def play_round(players):

    win_combo = [{4, 5, 6}, {1, 1, 1}, {2, 2, 2}, {3, 3, 3}, {4, 4, 4}, {5, 5, 5}, {6, 6, 6}]
    current_player = 0
    winning_player = None
    bets = players
    turns = 0

    while True:
        turns += 1
        if current_player == winning_player:
            turns -= 1
            break
        dice = roll_dice(3)

        if dice in win_combo:
            if winning_player is None:
                winning_player = current_player
            else:
                winning_player = None
                bets += players

        current_player += 1
        current_player %= players

    return turns, bets

player_num = 20
sim_num = 1000
turn_time = 0.25
bet_value = 0.05

avg_time = [0] * player_num  # avg time for a round, minutes
avg_pot = [0] * player_num  # avg winning pot size, dollars

for i in range(2, player_num + 1):
    turns_tmp = 0
    bets_tmp = 0
    for j in range(sim_num):
        t, b = play_round(i)
        turns_tmp += t
        bets_tmp += b
    turns_tmp /= sim_num
    bets_tmp /= sim_num
    avg_time[i - 1] = turns_tmp * turn_time
    avg_pot[i - 1] = bets_tmp * bet_value

print(avg_time)
print(avg_pot)
