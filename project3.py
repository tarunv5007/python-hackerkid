# Password Guessing
password = "Hello@123"
while True:
    passwordInput = input("Enter the password : ")
    if passwordInput == password:
        print("Correct password.")
        break
    else:
        print("Incorrect password!")