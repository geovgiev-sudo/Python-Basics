actor_name = input()
points_from_academy = float(input())
number_of_graders = int(input())
points_received = 0
total_points = 0

for i in range(1, number_of_graders + 1):
    grader_name = input()
    points_from_grader = float(input())
    points_received += len(grader_name) * points_from_grader / 2

    total_points = points_from_academy + points_received

    if total_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee '
              f'for leading role with {total_points:.1f}!')
        break

if total_points < 1250.5:
    points_needed = 1250.5 - total_points
    print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')