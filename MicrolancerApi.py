import Microlancer
import json

EMAIL = input('Enter your email: ')
PASSW = input('Enter your password: ')

print(EMAIL, file=open("login.txt", "a"))
print(PASSW, file=open("login.txt", "a"))

Login = Microlancer.Login(EMAIL, PASSW)

Login.login()

print("Menu:")
print("")
print("1. Show User Details")

choice = input('Select an option: ')

if choice == '1':
    details = Microlancer.Current()

    ID = json.dumps(details['id'])
    print("UserID:", ID)
    
    Username = json.dumps(details['username'])
    print("Username:", Username)

    print("Email:", EMAIL)

    Bio = json.dumps(details['bio'])
    print("Biography:", Bio)

    MemberSince = json.dumps(details['memberSince'])
    print("Member Since:", MemberSince)

    Balance = json.dumps(details['balance'])
    print("Balance:", Balance, "satoshis")

    gauth = json.dumps(details['googleAuthEnabled'])
    print("2-Factor-Authentication Enabled:", gauth)
