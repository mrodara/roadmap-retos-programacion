current_users = ['Mrodara', 'YGUILOP', 'arodGUI', 'admin', 'guest']
new_users = ['yguilop', 'arodgui', 'user1', 'user2', 'user3']

lower_users = [user.lower() for user in current_users]

print(lower_users)

for user in new_users:
    if user.lower() in lower_users:
        print(f"The username {user} has been used, you need to choose another one")
    else:
        print(f"The username {user} is available!!!")
        
        