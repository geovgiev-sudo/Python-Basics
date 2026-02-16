company_name = input()
adult_tickets = int(input())
child_tickets = int(input())
adult_ticket_price = float(input())
child_ticket_price = adult_ticket_price * 0.30
service_fee = float(input())


total_tickets = (adult_tickets * (adult_ticket_price + service_fee)
                 + child_tickets * (child_ticket_price + service_fee))
total_agency_gain = total_tickets - total_tickets * 0.80

print(f'The profit of your agency from {company_name} tickets is {total_agency_gain:.2f} lv.')
