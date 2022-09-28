name=input("What is your name? \n")
allowedUsers=["seyi","Emeka","Mike","Love"]
allowedPassword= ["passwordSeyi","passwordEmeka","paswwordMike","passwordLove"]
balance=300


if name in allowedUsers:
    password=input("Enter password: \n")
    #prints name position
    userId=allowedUsers.index(name)

    if password==allowedPassword[userId]:

        print("You are now logged in %s" % name)
        print("These are the available options: ")
        print("1. Withdrawal")
        print("2. cash Deposit")
        print("3. Complaints")

        selectedOption=int(input("Please select an option: \n"))

        if selectedOption ==1:
            print("You selected %s for withdrawal" % selectedOption)
            withdraw=int(input("How much Do you want to withdraw: \n"))

            if withdraw<balance:
                balance -=withdraw
                print("your new balance is %s" % balance)
            else:
                print("Insufficient funds")
            pass
        elif selectedOption ==2:
            print("You selected %s for cash deposit" % selectedOption)
            deposit=int(input("Enter amount to deposit: \n"))
            
            if deposit>0:
                balance+=deposit
                print("Deposit made successful ")
                print("Your new balance is %s" % balance)
            else:
                print("Amount to be deposited mmust be greater than 0")
            pass
        elif selectedOption ==3:
            print("You selected %s for complaints " % selectedOption)
            complaints=input("Kindly state your complaints: \n")
            print("Our staffs have take note of your complaints which is \n %s" % complaints)
            pass
        else:
            print("Inalid option selected, please try again")

    else:
        print("Invalid Password")

else:
    print("name doesnt exist in our database")
