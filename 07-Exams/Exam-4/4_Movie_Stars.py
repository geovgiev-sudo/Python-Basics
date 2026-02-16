actors_budget = float(input())
reward = 0
command = input()


while command != 'ACTION':
    actor_name = command
    reward = actors_budget * 0.20
    if len(actor_name) <= 15:
        reward = float(input())

    actors_budget -= reward

    if actors_budget <= 0:
        print(f'We need {abs(actors_budget):.2f} leva for our actors.')
        break

    command = input()

else:
    print(f'We are left with {actors_budget:.2f} leva.')