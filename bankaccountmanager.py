import mysql.connector as ms
db=ms.connect(host="localhost",user="root",passwd="louis333",database="bank")
cur=db.cursor()
home = "y"
subhome = "y"
while home=='y':
    opt = input("""Enter what you want to do \nCalculate-(1)inflation,(2)tax payments \nEnquire about (3)Different Types of loans with thier interest
    (4)Account opening procedure (5)Reward points and their redeem centres (6)Unblock/Block Features of Account or Card (7)Admin (8)Transaction Histroy""")
    def search1():
        query = "select * from {} where Name='{}'".format(ntable, name)
        cur.execute(query)
        data1 = cur.fetchall()
        query2 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{}'".format(ntable)
        cur.execute(query2)
        data2 = cur.fetchall()
        for i in range(len(data2)):
            print(data2[i][0], "=", data1[0][i])
    if opt == "7":
        while subhome=='y':
            na = input("password")
            if na == "bank@78":
                print("Welcome")
                opt1 = input(
                    "What you want to (1)search Account details (2)Edit account details (3)Add new user details(4)search in loan credit(5) edit loan credit,(6)add loan credit")
                ntable = "cust1"
                if opt1 == "1":
                    name = input("What is name of customer to search for")
                    search1()
                    home = input("Do you want to go to Main Menu y/n")
                if opt1 == "2":
                    name = input("what is name of customer to edit information for")
                    print("existing data of customer")
                    search1()
                    opta = input("\nDo you want to (0)update or (1)delete")
                    if opta == "0":
                        query2 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='cust1'"
                        cur.execute(query2)
                        data2 = cur.fetchall()
                        for i in range(len(data2)):
                            print("(", i, ")", data2[i][0], end="")
                        opt2 = input("which column to edit information for")
                        if opt2 == "0":
                            field = 'Name'
                        if opt2 == "1":
                            field = 'Balance'
                        if opt2 == "2":
                            field = 'Type_of_Account'
                        if opt2 == "3":
                            field = 'Joined_on'
                        if opt2 == "4":
                            field = "Interest Rate"
                        if opt2 in ["1", '2', "3"]:
                            newval = input("Enter the new value")
                        if opt2 == "4":
                            newval = float(input("Enter the new value"))
                        query = "update cust1 set {a}='{b}' where Name='{c}'".format(a=field, b=newval, c=name)
                        cur.execute(query)
                        db.commit()

                    if opta == "1":
                        query = "delete from cust1 where Name='{}'".format(name)
                        cur.execute(query)
                        db.commit()

                if opt1 == "3":
                    print("Pls Note if no value is the for a field then enter NULL")
                    name = input("Enter the name of new user")
                    balance = int(input("Enter the balance of the user"))
                    typeofac = input("Enter the type of Account")
                    joinon = input("Enter the Date of Join in format YYYY-MM-DD")
                    irate = float(input(
                        "Enter the Interest"))  # specific default interest for specific types of account and amount like if above 10lakh 5.2% and for F.D 5.7%
                    query = "insert into cust1 values('{a}',{b},'{c}','{d}',{e})".format(a=name, b=balance, c=typeofac,
                                                                                         d=joinon, e=irate)
                    cur.execute(query)
                    db.commit()

                if opt1 == "4":
                    name = input("What is name of customer to search for")
                    ntable = 'Credit'
                    search1()

                if opt1 == "5":
                    name = input("What is name of customer to edit details for")
                    ntable = 'Credit'
                    print('Existing Details of Customer')
                    search1()
                    opta = input("\nDo you want to (0)update or (1)delete")
                    if opta == "0":
                        query2 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='credit'"
                        cur.execute(query2)
                        data2 = cur.fetchall()

                        for i in range(len(data2)):
                            print("(", i, ")", data2[i][0], end="")
                        opt2 = input("which column to edit information for")
                        if opt2 == "0":
                            field = 'Name'
                        if opt2 == "1":
                            field = 'Phone_No'
                        if opt2 == "2":
                            field = 'Address'
                        if opt2 == "3":
                            field = 'Taken_Credit'
                        if opt2 == "4":
                            field = 'Credit_Left'
                        if opt2 == "5":
                            field = 'Interest_rate'
                        if opt2 == "6":
                            field = 'Monthly_Paid'
                        if opt2 == "7":
                            field = 'NotPaid_Months'
                        if opt2 == "8":
                            field = 'Credit_Taken_Date'
                        if opt2 == "9":
                            field = 'Credit_Closing_Date'
                        if opt2 == "10":
                            field = 'passkey'
                        if opt2 in ['1', '2', '3', '4', '6', '7', '8', '9', '10']:
                            newval = input("Enter the new value")
                        if opt2 == '5':
                            newval = float(input("Enter the new value"))
                        query = "update credit set {a}='{b}' where Name='{c}'".format(a=field, b=newval, c=name)
                        cur.execute(query)
                        db.commit()
                    if opta == "1":
                        query = "delete from cust1 where Name='{}'".format(name)
                        cur.execute(query)
                        db.commit()
                subhome = 'n'
            else:
                subhome = 'y'


            if opt1 == '6':
                print("Pls Note if no value is the for a field then enter NULL")
                name = input("Enter the name of customer")
                phoneno = input("Enter the phone no of customer")
                address = input("Enter the address of customer")
                tcredit = input("Enter the taken credit")
                creditl = input("Enter the credit left")
                irate = float(input("Enter the interest rate"))
                monthlypay = input("Enter the monthly payment")
                nopaidmonths = input("Enter the not paid months")
                tcreditdate = input("Enter the credit taken date")
                cdate = input("Enter the credit closing date")
                passkey = input("Enter the passkey")
                query = "insert into credit values('{a}','{b}','{c}',{d},{e},{f},{g},'{h}','{i}','{j}','{k}')".format(
                    a=name, b=phoneno, c=address, d=tcredit, e=creditl, f=irate, g=monthlypay, h=nopaidmonths,
                    i=tcreditdate, j=cdate, k=passkey)
                cur.execute(query)
                db.commit()
    if opt == "6":
        while subhome == "y":
            ntable = "features"
            pass1 = input("Enter your passkey")
            query = "select passkey from features"
            cur.execute(query)
            data = cur.fetchall()
            for i in range(len(data)):
                if data[i][0] == pass1:
                    status = "ok"
                else:
                    status='notok'
            if status == "ok":
                query1 = "select Name from features where passkey='{}'".format(pass1)
                cur.execute(query1)
                data1 = cur.fetchone()
                name = data1[0]
                search1()
                query1 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='features'"
                cur.execute(query1)
                data1 = cur.fetchall()
                for i in range(2, len(data1)):
                    print("(", i, ")", data1[i][0], end="")
                fi = input("\n Enter which field you want to change")
                if fi == '2':
                    field = 'Debit_Card'
                if fi == '3':
                    field = 'Swipe'
                if fi == '4':
                    field = 'UPI'
                if fi == '5':
                    field = 'RFID_Pay'
                if fi == '6':
                    field = 'passkey'
                newval = input("To enable enter Y to disable enter N ")
                query = "update features set {a}='{b}' where Name='{c}'".format(a=field, b=newval, c=name)
                cur.execute(query)
                db.commit()
                subhome = "n"

            if status == 'notok':
                print('Wrong Passkey')
                subhome = 'y'

    if opt == '5':
        ntable = 'Reward_List'
        rpoints = int(input("How much reward points do you have"))
        query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{}'".format(ntable)
        cur.execute(query)
        data = cur.fetchall()
        for i in data:
            print(i[0], end="         ")
        query = "select * from Reward_List where Reward_Points_Needed<={}".format(rpoints)
        cur.execute(query)
        data = cur.fetchall()
        for i in data:
            print("\n", i)
    if opt == "4":
        acc = input("Which account you want to open (0)Savings,(1)Fixed Deposit,(2)Foreign Exchange")
        if acc == "0":
            myfile = open('Savings.txt', 'r')
            for line in myfile:
                print(line)
        if acc == "1":
            myfile = open('FD.txt', 'r')
            for line in myfile:
                print(line)
        if acc == '2':
            myfile = open('Forex.txt', 'r')
            for line in myfile:
                print(line)
    if opt == '3':
        ntable = 'loans'
        def search2():
            query = "select * from loans where Types_Of_Loans='{}'".format(field)
            cur.execute(query)
            data1 = cur.fetchall()
            for i in range(len(data)):
                print(data[i][0], "=", data1[0][i])
        query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{}'".format(ntable)
        cur.execute(query)
        data = cur.fetchall()
        loan = input("Which loan do you want to take (1)Home Loan,(2)Vehicle Loan,(3)LandLoan,(4)All Loans")
        if loan == "1":
            field = 'Home_Loan'
            search2()
        if loan == "2":
            field = 'Vechicle_Loan'
            search2()
        if loan == "3":
            field = 'Land_Loan'
            search2()
        if loan == "4":
            field = 'Home_Loan'
            search2()
            field = 'Vechicle_Loan'
            search2()
            field = 'Land_Loan'
            search2()
    if opt=="2":
        income=int(input("Enter your monthly income"))
        yincome=income*12
        if yincome<250000:
            print("You dont have to pay income tax")
        if yincome>250000 and yincome<=500000:
            tax=5/100
            itax=yincome*tax
            print("Your income tax is 5% of your income so you have to pay",itax)
        if yincome>500000 and yincome<=750000:
            tax=10/100
            itax=yincome*tax
            print("Your income tax is 10% of your income so you have to pay",itax)
        if yincome>750000 and yincome<=100000:
            tax=15/100
            itax=yincome*tax
            print("Your income tax is 15% of your income so you have to pay",itax)
        if yincome>1000000 and yincome<=1250000:
            tax=20/100
            itax=yincome*tax
            print("Your income tax is 20% of your income so you have to pay", itax)
        if yincome>1250000 and yincome<=1500000:
            tax=25/100
            itax=yincome*tax
            print("Your income tax is 25% of your income so you have to pay", itax)
        if yincome>1500000:
            tax=30/100
            itax=yincome*tax
            print("Your income tax is 30% of your income so you have to pay", itax)
    if opt=="1":
        opt2=input("Do you want to calculate for past year(p) or future year(f)")
        def infla():
            global amount
            amount = int(input("Enter the amount you want to calculate inflation for"))
            query = "select cpi from inflation where observation_date='2022-07-01'"
            cur.execute(query)
            data = cur.fetchall()
            global ecpi
            ecpi = data[0][0]
            query = "select cpi from inflation where observation_date='{}'".format(year)
            cur.execute(query)
            data = cur.fetchall()
            global scpi
            scpi = data[0][0]
        if opt2=="p":
            year = input("Enter the year you want to calculate inflation for in format YYYY-MM")
            year = year + "-01"
            infla()
            irate = scpi / ecpi
            famount = amount * irate
            print(amount, "will be", famount, "in the year", year)
        if opt2=="f":
            print("Future inflation calculation is based on past change rate and will only aprrox value because of many factors")
            year1= int(input("Enter the year you want to calculate inflation for in format YYYY"))
            year2=year1-2022
            year=str(2022-year2)+'-07-01'
            infla()
            irate = ecpi / scpi
            famount = amount * irate
            famount+=famount*0.21376312206              #Calculating with error factor
            print(amount, "will be", famount, "in the year", year1)
    if opt=="8":
        while subhome=='y':
            pass1 = input("Enter the passkey of your account")
            query="select passkey from transactions"
            cur.execute(query)
            data=cur.fetchall()
            status=""
            for i in data:
                if i[0]==pass1:
                    status="ok"
            if status=='ok':
                query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='transactions'"
                cur.execute(query)
                data = cur.fetchmany(9)  # Fectching every column is must or else it will show error
                for i in data:
                    print(i[0], end='    |    ')
                query = "select * from transactions where passkey='{}'".format(pass1)
                cur.execute(query)
                data = cur.fetchall()
                print(
                    '\n------------------------------------------------------------------------------------------------------------------------------------------------------------')
                for i in data:
                    for j in range(len(i)):
                        if j == 0:
                            print(i[j], end='       ')
                        if j == 1:
                            print(i[j], end='             ')
                        if j == 2:
                            print(i[j], end='              ')
                        if j == 3:
                            print(i[j], end="                    ")
                        if j == 4:
                            print(i[j], end='         ')
                        if j == 5:
                            print(i[j], end='    ')
                        if j == 6:
                            print(i[j], end='     ')
                        if j == 7:
                            print(i[j], end="      ")
                        if j == 8:
                            print(i[j])
                subhome="n"
                print('\n')
            else:
                print("wrong passkey")
    home = input("Do you want to go to Main Menu y/n")
print("Thank you for using our program  (•◡•)/")
db.close()
