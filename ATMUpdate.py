from datetime import datetime
import random
database = {5003801702: ['theo', 'Theophilus Okolie', 'theo', 'theo@theo.com', 9230, 5003801702], 9649055469: ['Chii', 'Chii Bekee', 'chii', 'chii@chi.com', 478, 9649055469]}
newdatabase = {}
def oldcustomer():
    print ("Welcome")
    UniqueAccount = int(input ("What is your Account Number? Enter 0 to Exit \n"))

    if UniqueAccount in database.keys():
        password = input ("Your password? \n")
        for UniqueAccount in database.values():
            if(password == UniqueAccount[2]):
                Operations(UniqueAccount)
            else:
                print ('Password incorrect, Please try again')
                oldcustomer ()
    elif UniqueAccount in newdatabase.keys():
        password = input ("Your password? \n")
        for UniqueAccount in newdatabase.values():
            if(password == UniqueAccount[2]):
                Operations(UniqueAccount)
            else:
                print ('Password incorrect, Please try again')
                oldcustomer ()
    elif (UniqueAccount == 0):
        quit ()
    else:
        print('Account Does not Exist, Please try again')
        oldcustomer()
def Operations(UniqueAccount):
    print ("Welcome %s" %  UniqueAccount[1] + " the time is " + str(datetime.now()))
    print ("Your account number is %s and your Current Balance is %d " % (UniqueAccount[5], UniqueAccount[4]))
    print('1. Withdrawal')
    print('2. Deposit')
    print('3. Complaint')
    print('4. Quit/Logout')

    selectedOption = int(input("Please select an option: "))

    if (selectedOption == 1):
        withdrawal = int (input ("How much would you like to Withdraw? "))
        if (withdrawal <= UniqueAccount[4]):
            UniqueAccount[4] -= withdrawal 
            print ("take your cash")
            print ("Your remaining balance is %d" % UniqueAccount[4])
        else:
            print ("Not enough Balance")
    
    elif (selectedOption == 2):
        deposit = int(input ("How much would you like to Deposit? "))
        UniqueAccount[4] += deposit
        print ("Your current balance is %d" % UniqueAccount[4])

    elif (selectedOption == 3):
        complaint = input ("What issue would you like to report? \n")
        print ("Thank you for contacting us")
    
    elif (selectedOption == 4):
        logout()

    else: 
        print ("Invalid Option Selected, please try again")
    Operations(UniqueAccount)
def NewUser():
    print("****** Register *******")
    username = input("Choose a Username? \n")
    Fullname = input("Enter your Full Name? \n")
    password = input("create a password for yourself \n")
    email = input("Enter your Email Address \n")
    newuserno = generateuserno()
    balance = 0
    
    newdatabase[newuserno] = [username, Fullname, password, email, balance, newuserno]


    print("Your Account Creation was successful")
    print("*****************************")
    print("Dear %s Your account number is: %d" % (Fullname, newuserno))
    print("Make sure you keep it safe")
    print("You can proceed to Login")
    
    
    Welcome()
def generateuserno():
    return random.randrange(100000000, 9999999999)
def logout():
    print("\n You have logged Out")
    Welcome()
def Welcome():
    WelcomeOption = input("Welcome to Zuri Bank Plc \n New Customer? Press 1 \n Existing Customer? Press 2 \n Enter 0 to Quit \n")
    if (WelcomeOption == 1 or WelcomeOption == '1'):
        NewUser()
    elif (WelcomeOption == 2 or WelcomeOption == '2'):
        oldcustomer()
    elif (WelcomeOption == 0 or WelcomeOption == '0'):
        quit()
    else:
        print ("\n Please Enter a Valid Option \n")
    Welcome()
Welcome() 