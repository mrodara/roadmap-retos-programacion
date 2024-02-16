usernames = ['mrodara', 'yguilop', 'arodgui', 'admin']

username = input("Introduce your username: ")

if usernames:
    if username in usernames:
        if username.lower() == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f"Hello {username}, thank you for loggin in again")
    else:
        print("Sorry you're not registered yet.")
else:
    print("There are no users registered yet")