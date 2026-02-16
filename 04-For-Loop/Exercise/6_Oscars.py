actor_name = input()
points_from_academy = float(input())
graders_count = int(input())

points_received = points_from_academy + 0

for i in range(graders_count):
    grader_name = input()
    points_from_grader = float(input())
    points_received += (len(grader_name) * points_from_grader) / 2

    if points_received >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {points_received:.1f}!')
        break

else:
    points_needed = 1250.5 - points_received
    print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')