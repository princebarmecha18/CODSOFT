import random
def password_generator (length):
    password=""
    for i in range(length):
        password += chr(random.randint(33,122))        #Uses 33 to 122 ASCII Value
    return password

while True:
    try:
        pass_len=int(input("Enter Length of Password Required (min 8): "))
    
    except ValueError:
        print("Invalid Input , Please enter a number greater than 8")

    if pass_len >= 8:
        user_pass = password_generator(pass_len)
        print (user_pass)
        break
    
    else:
        print("To ensure passwords are strong and secure minimum of 8 characters is required.")
    
    



