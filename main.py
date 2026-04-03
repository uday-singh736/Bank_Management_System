import mysql.connector   #importing connector
h=input("Enter the mysql host name (Default='localhost'):")
u=input("Enter your mysql user name (Default='root'):")
p=input("Enter your mysql password:")
conn=mysql.connector.connect(host='{}'.format(h),\
                             user='{}'.format(u),passwd='{}'.format(p))
cu_sr=conn.cursor()
def main(): 
    print("Python is connected to mysql successfully!!!!!!!!")
    cu_sr.execute("create database if not exists Bank")     #creating tables
    cu_sr.execute("use Bank")
    cu_sr.execute("create table if not exists account(name varchar(20),\
                   ac_no int(100) primary key,\
                   dob date,\
                   add_ss varchar(34),\
                   open_amount int(20))")
    cu_sr.execute("create table if not exists balance(name varchar(20),\
                   ac_no int(100) primary key,\
                   balance int(25))")
    print('''======================================================================================
======================================================================================''','\n')
    print("                   SBS _BANK _MANAGEMENT_ _SYSTEM                ","\n")
    print('''======================================================================================
======================================================================================''',"\n")
    print("1.LOGIN") #logging in
    print("2.Exit")
    choice=int(input("Enter your  choice")) 
    print('''======================================================================================
======================================================================================''','\n')
    if choice==1:
        print("=====================successfully loged in============================================")
        print("WELCOME USER")
        print("1.press 1 to open new account.")
        print("2.press 2 to debit money")
        print("3.press 3 to make transactions")
        print("4.press 4 to check balance")
        print("5.press 5 to get your details ")
        print("6.press 6 to TRANSFER money")
        print("7.press 7 to get latest information about schemes.")
        print("8.press 8 to remove your account")
        print("9.press 9 to exit")
        choice=int(input("Enter TASK no.")) #taking tasks from user (input)
        if choice == 1:
                    open_account()
        elif choice==2:
            debit()
        elif choice==3:
            withdraw()
        elif choice==4:
            check()
        elif choice==5:
            details()
        elif choice==6:
            Transfer()
        elif choice ==7:
            info()
        elif choice==8:
            del_acc()
        elif choice==9:
            print("LOGGED OUT SUCCESSFULLY")
            exit()
        else:
            exit()
    else:
        exit() #exiting
            
def open_account(): #creating new account in bank
    nm=input("enter your name : ")
    ac=int(input("Enter account number (as provided by bank itself):"))
    d_b=input("enter your date of birth(yyyy-mm-dd):")
    addss=input("Enter you residential address:")
    at=int(input("Enter your amount with which you will open account:"))
    query="INSERT INTO account values('{}',{},'{}','{}',{})".format(nm,ac,d_b,addss,at)
    cu_sr.execute(query) #Executing query
    DATA=nm,ac,at
    quer_y="INSERT INTO balance values('{}',{},{})".format(nm,ac,at) #inserting data
    cu_sr.execute(quer_y)
    conn.commit()
    print("YOUR ACCOUNT HAS BEEN SUCCESSFULLY OPENED......!")
def debit(): #debit amount
    ac=int(input("Enter your account no:"))
    query="select * from balance where ac_no={}".format(ac,)
    cu_sr.execute(query)
    record=cu_sr.fetchone()
    if record != None:
           amt=int(input("Enter the amount to be debited"))
           query="update balance set balance=balance+{} where ac_no={}".format(amt,ac) 
           cu_sr.execute(query)#updating balance
           conn.commit()
           print("------------------------processing--------------")
           print("------------------------wait-------------------")
           print("Amount successfully debited")
    else:
        print("oops! sorry may be wrong account number ...try again ....")
def withdraw(): #withdrawing amount
    ac=int(input("Enter your account no:"))  
    query="select * from balance where ac_no={}".format(ac,)
    cu_sr.execute(query)
    record=cu_sr.fetchone() #fetching from relation
    if record != None:
           amt=int(input("Enter the amount to be withdraw"))
           query="update balance set balance=balance-{} where ac_no={}".format(amt,ac)
           cu_sr.execute(query)
           conn.commit()
           print("------------------------processing--------------")
           print("------------------------wait-------------------")
           print("Amount successfully credited")
    else:
        print("oops! sorry may be wrong account number ...try again ....")
def check(): #checking balance
    ac=int(input("Enter your account no:"))
    query="select * from balance where ac_no={}".format(ac,)
    cu_sr.execute(query)
    record=cu_sr.fetchone()
    if record != None:
           print("your balance is...","\n")
           query="select balance from balance where ac_no={}".format(ac)
           cu_sr.execute(query)
           record=cu_sr.fetchone()
           print(record[0]) #getting balance from acount
    else:
        print("oops! sorry may be wrong account number ...try again ....")
def details(): #All stored data in bank server
    ac=int(input("Enter your account no:"))
    query="select * from account where ac_no={}".format(ac,)
    cu_sr.execute(query)
    record=cu_sr.fetchone()
  
    if record != None:
           b=("NAME\t\t","Account_number\t","Date_of_birth\t","address\t","Open_amount\t")
           a=[]
           print("DETAILS ARE AS FOLLOWS:")
           for i in record:
               a.append(i)
          
           for i in range(len(b)):
               print(b[i]+str(a[i]))
    else:
        print("oops! sorry may be wrong account number ...try again ....")
    
def Transfer(): #Transfer money
    ac1=int(input("Enter your account no:"))
    ac2=int(input("Enter account no. of person to whom payment is to be made"))
    query="select * from balance where ac_no={} or ac_no={}".format(ac1,ac2)
    cu_sr.execute(query)
    record1=cu_sr.fetchone()
    record2=cu_sr.fetchone()
    if record1 != None and record2 !=None:
        amt=int(input("Enter the amount to be transfered:"))
        query="update balance set balance=balance-{} where ac_no={}".format(amt,ac1)
        cu_sr.execute(query)
        query2="update balance set balance=balance+{} where ac_no={}".format(amt,ac2)
        print("====MONEY BEING TRANSFERRD=========")
        print("PROCESS COMPLETE..............")
    else:
        print("oops! sorry may be wrong account number ...try again ....")
        
def del_acc(): #removing account
     ac=int(input("Enter your account no:"))
     query="select * from balance where ac_no={}".format(ac,)
     cu_sr.execute(query)
     record=cu_sr.fetchone()
     if record != None:
            query="delete from account where ac_no={}".format(ac)
            query2="delete from balance where ac_no={}".format(ac)
            cu_sr.execute(query2)
            cu_sr.execute(query)
            conn.commit()
            print("ACCOUNT SUCCESSFULLY REMOVED FROM SERVER.")
     else:
         print("oops! sorry may be wrong account number ...try again ....")
            
def info(): #getting information about latest schemes
    print(" Some of the important schemes are:")
    print("==============================================================================")
    print("==============================================================================")
    print("1.NATIONAL PENSION scheme")
    print("TO KNOW ABOUT IT PRESS 1")
    print("2.public provident fund")
    print("TO KNOW ABOUT IT PRESS 2")
    print("3.CAPITAL GAINS A/C SCHEME") 
    print("TO KNOW ABOUT IT PRESS 3")
    print("4.Gold banking")
    print("TO KNOW ABOUT IT PRESS 4")
    choice=int(input("make your choice"))
    if choice== 1:
        f=open("NPS.txt","r") #fetching texts from text files
        print(f.read())
    elif choice==2:
        f=open("ppf.txt",)
        print(f.read())
    elif choice==3:
        f=open("cgs.txt","r")
        print(f.read())
    elif choice==4:
        f=open("gb.txt","r")
        print(f.read())
    else:
        print("=========exiting page===========")
        exit()
main() #calling main fuunction
    
    

    
           
    
    
