# if ma true statement else ma false ma hunxa statement
# branching garni condition halara


# login code 

email = input("Enter your email: ")


if '@' in email:

    if email == 'abc@gmail.com':
        password = int(input("Enter your password in Number integer: "))
        if password == 1234:
            print("Login Successfully")
        else:
            print("Password is incorrect")
            tpassword = int(input('Again enter the password for 2nd chance: '))
            if tpassword == 1234:
                print('Finally login')
            else:
                print('Wrong and login failed error')
    else:
        print("Email does not match")

else:
    print("email pattern doesnot match")