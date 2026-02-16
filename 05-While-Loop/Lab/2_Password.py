username = input()
password = input()
password_try = input()

while password_try != password:
    password_try = input()

print(f'Welcome {username}!')

# while True:
#     new_password = input()
#     if new_password != password:
#         new_password = input()
#     else:
#         print(f'Welcome {username}!')
#         break
#