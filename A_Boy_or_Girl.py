username = input().strip()
user = set(username)
length = len(user)
if length % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")