# import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import functions as f

while True:
    print("\n")
    print("1. Analyze Student")
    print("2. Compare Students")
    print("3. Analyze Batch")
    print("4. Compare Batch")
    print("5. Analyze Branch")

    print("6. Compare Branch")
    print("7. Exit")
    print("-----------------X-----------------")

    while True:
        print("\n")
        choice=int(input("Enter Your Choice : "))
        print("\n")
        if 0 < choice < 8:
            break
        else:
            print("Invalid Choice !!!")

    if choice==1: #Analyze Student

        flag=True
        while flag:
            Roll=int(input("Enter the Roll Number Of Student : "))
            if Roll>0 and Roll<266:
                flag=False
            else:
                print("Enter Roll Number Between 1 to 265 !!!")
        f.analyze_student(Roll)

    elif choice==2: #Compare Students

        flag=True
        while flag:
            Roll_1=int(input("Enter the Roll Number Of Student 1: "))
            print("\n")
            if Roll_1>0 and Roll_1<266:
                flag=False
            else:
                print("Enter Roll Number Between 1 to 265 !!!")
        flag=True
        while flag:
            Roll_2=int(input("Enter the Roll Number Of Student 2: "))
            if Roll_2>0 and Roll_2<266:
                flag=False
            else:
                print("Enter Roll Number Between 1 to 265 !!!")

        f.compare_students(Roll_1,Roll_2)

    elif choice==3:     #Analyze Batch

        flag=True
        while flag:
            Batch=input("Enter the Batch(1 to 8) : ")
            if  0 < int(Batch) <9 :
                flag=False
                Batch="B"+Batch
            else:
                print("Enter Batch Between 1 to 8 !!!")

        f.analyze_batch(Batch)

    elif choice==4:     #Compare Batch
        
        flag=True
        while flag:
            Batch_1=input("Enter the Batch(1 to 8) : ")
            print("\n")
            if  0 < int(Batch_1) <9 :
                flag=False
                Batch_1="B"+Batch_1
            else:
                print("Enter Batch Between 1 to 8 !!!")
        flag=True
        while flag:
            Batch_2=input("Enter the Batch(1 to 8) : ")
            if  0 < int(Batch_2) <9 :
                flag=False
                Batch_2="B"+Batch_2
            else:
                print("Enter Batch Between 1 to 8 !!!")

        f.compare_batch(Batch_1,Batch_2)
        
    elif choice==5:     #Analyze Branch
        flag=True
        while flag:
            Branch=input("Enter the Branch( CSE / CEA / CST / IT ) : ")
            if  Branch.upper() in ["CSE","CEA","CST","IT"] :
                Branch=Branch.upper()
                flag=False
            else:
                print("Enter Only Available Branch !!!")
        f.analyze_branch(Branch)
        

    elif choice==6:     #Compare Branch

        flag=True
        while flag:
            Branch_1=input("Enter the Branch(CSE / CEA / CST / IT) : ")
            print("\n")
            if  Branch_1.upper() in ["CSE","CEA","CST","IT"] :
                Branch_1=Branch_1.upper()
                flag=False
            else:
                print("Enter Only Available Branch !!!")
        flag=True
        while flag:
            Branch_2=input("Enter the Branch(CSE / CEA / CST / IT) : ")
            if  Branch_2.upper() in ["CSE","CEA","CST","IT"] :
                Branch_2=Branch_2.upper()
                flag=False
            else:
                print("Enter Only Available Branch !!!")

        f.compare_branch(Branch_1,Branch_2)

    elif choice==7:
        f.Get_Toppers()
    elif choice==7:
        break
    else:
        print("Invalid Choice !!!")
        continue