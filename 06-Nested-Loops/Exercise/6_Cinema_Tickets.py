student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

while True:
    film_name = input()

    if film_name == 'Finish':
        print(f'Total tickets: {total_tickets}')
        protzent_student = student_tickets / total_tickets * 100
        protzent_standard = standard_tickets / total_tickets * 100
        protzent_kid = kid_tickets / total_tickets * 100
        print(f'{protzent_student:.2f}% student tickets.')
        print(f'{protzent_standard:.2f}% standard tickets.')
        print(f'{protzent_kid:.2f}% kids tickets.')
        break

    free_spaces = int(input())
    tickets_sold = 0

    while True:
        if tickets_sold == free_spaces:
            break

        ticket_type = input()

        if ticket_type == 'End':
            break

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1

        tickets_sold += 1
        total_tickets += 1

    protzent_tickets_sold = tickets_sold / free_spaces * 100
    print(f'{film_name} - {protzent_tickets_sold:.2f}% full.')