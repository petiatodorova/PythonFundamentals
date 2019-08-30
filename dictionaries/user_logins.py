line = input().split(" -> ")

user_pass = {}
count_unsuccessfull_attempts = 0

while not (line[0] == "login"):
    key_user = line[0]
    value_pass = line[1]
    user_pass[key_user] = value_pass
    line = input().split(" -> ")

line = input().split(" -> ")
while not (line[0] == "end"):
    key_user = line[0]
    value_pass = line[1]
    if (key_user in user_pass) and (user_pass[key_user] == value_pass):
        print(f"{key_user}: logged in successfully")
    if not (key_user in user_pass) or not (user_pass[key_user] == value_pass):
        print(f"{key_user}: login failed")
        count_unsuccessfull_attempts += 1
    line = input().split(" -> ")

print(f"unsuccessful login attempts: {count_unsuccessfull_attempts}")