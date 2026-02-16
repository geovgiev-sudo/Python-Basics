tournament_days = int(input())
money_total = 0
total_wins = 0
total_lose = 0

for games in range(1, tournament_days + 1):
    command = input()
    money_gained_day = 0
    games_won_day = 0
    games_lost_day = 0

    while command != 'Finish':
        sport = command
        result = input()
        if result == 'win':
            games_won_day += 1
            total_wins += 1
            money_gained_day += 20
        elif result == 'lose':
            games_lost_day += 1
            total_lose += 1

        command = input()

    if games_won_day > games_lost_day:
        money_gained_day *= 1.10
    money_total += money_gained_day

if total_wins > total_lose:
    money_total *= 1.20
    print(f'You won the tournament! Total raised money: {money_total:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {money_total:.2f}')