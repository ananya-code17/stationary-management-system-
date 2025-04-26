print("This is project-1 on: CUSTOMER INFORMATION MANAGEMENT SYSTEM \n\n")

def add():
    cid=input("Enter Customer ID: ")
    nm=input("Enter Customer Name: ")
    ad=input("Enter Customer Address: ")
    cn=input("Enter Contact No: ")
    f=open("C:\\Users\\HP\\OneDrive\\Documents\\Python Programming Files\\customer.txt","a")
    f.write(cid+"\t")
    f.write(nm+"\t")
    f.write(ad+"\t")
    f.write(cn+"\n")
    print("Record Added \n\n")
    f.close()

def delete():
    i=input("Enter the ID to remove from file: ")
    with open("C:\\Users\\HP\\OneDrive\\Documents\\Python Programming Files\\customer.txt","r") as f:
        all=f.readlines()
    with open("C:\\Users\\HP\\OneDrive\\Documents\\Python Programming Files\\customer.txt","w") as f:
        for data in all:
            d=data.split("\t",1)
            if(d[0]!=i):
                f.writelines(data)
    print("Record Deleted \n\n") 

def update():
    i=input("Enter the ID to be updated in the file: ")
    with open("C:\\Users\\HP\\OneDrive\\Documents\\Python Programming Files\\customer.txt","r") as f:
        all=f.readlines()
    with open("C:\\Users\\HP\\OneDrive\\Documents\\Python Programming Files\\customer.txt","w") as f:
        for data in all:
            d=data.split("\t",1)
            if(d[0]==i):
                nn=input("Enter New Name: ")
                na=input("Enter New Address: ")
                nc=input("Enter New Contact No.: ")
                f.writelines(d[0]+"\t"+nn+"\t"+na+"\t"+nc+"\n")
            else:
                f.writelines(data)
    print(" Record Updated \n\n")

def search():
    i=input("Enter the ID to be searched from file: ")
    with open("C:\\Users\\HP\\OneDrive\\Documents\\Python Programming Files\\customer.txt","r") as f:
        all=f.readlines()
        for data in all:
            d=data.split("\t",1)
            if(d[0]==i):
                print("searched data : \n",data)

def show():
    f=open("C:\\Users\\HP\\OneDrive\\Documents\\Python Programming Files\\customer.txt","r")
    print("ID\tNAME\tADDRESS\tCONTACT No.")
    print(f.read())
    f.close()

while(True):
    print("Welcome to Customer portal")
    print("1: ADD NEW CUSTOMER")
    print("2: DELETE CUSTOMER")
    print("3: UPDATE CUSTOMER")
    print("4: SEARCH CUSTOMER")
    print("5: SHOW ALL CUSTOMER")
    print("6: EXIT")
    ch=int(input("Enter your choice: "))
    if ch==1:
        add()
    elif ch==2:
        delete()
    elif ch==3:
        update()
    elif ch==4:
        search()
    elif ch==5:
        show()
    elif ch==6:
        break
    else:
        print("Invalid Choice: PLEASE ENTER ANOTHER CHOICE FROM 1-5")

    
        
