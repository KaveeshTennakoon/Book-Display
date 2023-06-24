Books_Owned=[]
Books_Needed=[]

def OwnBook():
    OwnedBooks=(input("Book Name: "))
    Books_Owned.append(OwnedBooks)
  

def NewBook():
    NeedBooks=(input("Book Name: "))
    Books_Needed.append(NeedBooks)
    

print("1: Enter owned books")
print("2: Enter needed books")
print("3: Output the results")
print("4: Exit")


choice=0
while choice !=4:
    print()
    choice=int(input("Enter your choice: "))
    print()

    if choice == 1:
        num=int(input("How many books are owned: "))
        for i in range(num):
            OwnBook()

    elif choice == 2:
        num=int(input("How many books are needed: "))
        for i in range(num):
            NewBook()        

    elif choice == 3:
        
        if len(Books_Owned)>len(Books_Needed):
            num=len(Books_Owned)
            num2=len(Books_Needed)
            for i in range(num2,num):
                Books_Needed.append("")
        else:
            num=len(Books_Needed)
            num2=len(Books_Owned)
            for i in range(num2,num):
                Books_Owned.append("")

        print("Owned\tNeeded")
        for elem1, elem2 in zip(Books_Owned, Books_Needed):
            print("{}\t{}".format(elem1, elem2))
        
    
print("Exiting program...")