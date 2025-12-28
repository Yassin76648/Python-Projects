import os
import time
class Member :
    def __init__(self , first_name , last_name , id , status = 'inactive') :
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.status = status

    def display_member(self):
        print("Member : ")
        print(f"First Name : {self.first_name}")    
        print(f"Last Name : {self.last_name}")    
        print(f"Member ID : {self.id}")            
        print(f"Status : {self.status}")    


def create_member():
    first_name = input("Enter First Name :")                        
    last_name = input("Enter Last Name :")                        
    id = input("Enter Member ID :")                        
    status = input("Enter MemberShip Status  [active , inactive], Or click Enter  : ")
    if status == "" :
        status = 'inactive'                        
    
    return Member(first_name , last_name ,  id , status)



# Create the clear_screen function first
def clear_screen():
        _ = os.system('cls')


print("__________  Welcome To Gym Membership Management  __________ ")

members_list = []

while True :
    option = input(""" 
1. Add New Member 
2. Display All Members
3. Search For Member 
4. Exit 
Select An Option : """)
    
    if option == "1" :
        clear_screen()
        member = create_member() 
        members_list.append(member)
        print("Member Added Succesfully")
        time.sleep(3)
        clear_screen()
    elif option == "2" :
        clear_screen()
        print("\nDisplaying All Members ... \n")
        for member in members_list :
            print("---------------------------------")
            member.display_member()
        time.sleep(5)
        clear_screen()
    elif option == "3" :
        clear_screen()
        choice = input("""
Search Member by : 
1. Membership ID
2. Membership Name 
3. Membership Status 

Select Your Option : """)
        if choice == "1" :
            clear_screen()
            id = input("Enter Membership ID : ")
            for member in members_list :
                if member.id == id :
                    print("Member Found ...")
                    member.display_member()
                print("Sorry , Member Not Founded")
            time.sleep(5)
            clear_screen()
        elif choice == "2" :
            clear_screen()
            name = input("Enter Membership Name : ")            
            for member in members_list :
                if member.first_name == name :
                    print("Member Found ...")
                    member.display_member()
            time.sleep(3)
        elif choice == "3" :
            clear_screen()
            status = input("Enter Membership status : ")            
            for member in members_list :
                if member.status == status :
                    print("Member/s Found ...")
                    member.display_member()
            time.sleep(3)
        else :
            print("Invalid Option , Please Try Again ... ")            