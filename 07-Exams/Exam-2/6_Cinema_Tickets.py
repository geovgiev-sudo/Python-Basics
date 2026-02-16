command = input()
ticket_type = ''
tickets_total = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while command != 'Finish':
    film_name = command
    tickets_sold = 0
    free_places = int(input())
    command2 = input()

    while command2 != 'End':
        ticket_type = command2
        tickets_sold += 1
        tickets_total += 1

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1

        if tickets_sold >= free_places:
            break

        command2 = input()

    protzent_full = tickets_sold / free_places * 100
    print(f'{film_name} - {protzent_full:.2f}% full.')

    command = input()

print(f'Total tickets: {tickets_total}')
protzent_student = student_tickets / tickets_total * 100
protzent_standard = standard_tickets / tickets_total * 100
protzent_kid = kid_tickets / tickets_total * 100
print(f'{protzent_student:.2f}% student tickets.')
print(f'{protzent_standard:.2f}% standard tickets.')
print(f'{protzent_kid:.2f}% kids tickets.')