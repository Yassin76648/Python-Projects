# To do list
# Add new task
# Display All tasks 
# mark task as complete
# quit

tasks = []
print("__________  Welcome To To-Do List Management  __________ ")
def main() :

    massage = """\n1. Add New Task 
2. Display All tasks 
3. Mark Task as Complete
4. Quit
    \n"""
    
    

    while True:
        print(massage)
        option = input("Enter Your Option : ")

        if option == "1" :
            add_task()
        elif option == "2" :
            print("Displaying Tasks ... \n")
            Display_tasks()
        elif option == "3" :
            mark_task_complete()
        elif option == "4" :
            break
        else:
            print("Invalid Choice , Please Try Again ... ")



def add_task() :
    name = input("Enter Task Name : ")
    deadline = input("Enter Task Deadline , (mm/dd/yyyy): ")
    status = 'incomplete'

    task_info = {"name" : name , "deadline" : deadline , "status" : status }
    tasks.append(task_info)
    print("Task Added Succesfully ... \n")

def Display_tasks() :
    if not tasks :
        print("No Tasks Available ... \n")
        return
    for task in tasks :
        print("\n-----------------------------")
        print(f"Task : {task["name"]}")
        print(f"Deadline : {task["deadline"]}")
        print(f"Status : {task["status"]}")
        print("-----------------------------")

def mark_task_complete():
    incomplete_tasks = []
    
    for task in tasks :
        if task["status"] == "incomplete" :
            incomplete_tasks.append(task)

    if incomplete_tasks == [] :
        print("No Incomplete Tasks ... ")
        return
    
    print("\nYour incompleted Tasks ... ")
    for i , task in enumerate(incomplete_tasks ,start=1) :
        
        print("\n-----------------------------")
        print(f"Task Number : {i}")
        print(f"Task : {task["name"]}")
        print(f"Deadline : {task["deadline"]}")
        print(f"Status : {task["status"]}")
        print("-----------------------------")

    
    try :
        task_no  = int(input("Enter the number Of the Task you want to mark as complete : "))
        if 1 <= task_no <= len(incomplete_tasks) :
            selected_task = incomplete_tasks[task_no -1]
            selected_task["status"] = "complete"
            print ("Marked ... ")
        else :
            print("Invalid Task Number ... ")    
    except ValueError :
        print("Invalid Input , Please Enter a Number ... ")
        
main()



