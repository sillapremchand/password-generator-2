chars = "abcdefkhmwolturejnyb12345678g90@!#$%^&*"

print("Welcome to the password generator")
length = int(input("Enter the length of your password:"))

for i in range(length):
    password = ""
    password = random.choice(chars)
    print(password)
