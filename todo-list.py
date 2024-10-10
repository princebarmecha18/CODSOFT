def add_tasks ():
    global tasks
    count= int(input("Enter The Number Of Tasks To be Added: "))
    for i in range(1,count+1):
        task=input(f"Enter Task {i}:").lower()
        tasks.append(task)
    display_tasks()
    
def delete_tasks():
    global tasks
    if tasks==[]:
        print("No Tasks Available. Add Tasks!")
    else:
        try:
            del_task=input("Enter The Task To Delete/Complete: ").lower()
            tasks.remove(del_task)
            print("Deleted Successfully.")
            display_tasks()
        except ValueError:
            print(del_task,"was not found/added in the list.")
   
def update_tasks():
    global tasks
    update_task=input("Enter The Task Which Needs To Be Updated: ").lower()
    if update_task in tasks:
        indx=tasks.index(update_task)
        updated_task=input("Enter The New Task: ").lower()
        tasks[indx]=updated_task
    print("Updated Your List.\n")
    display_tasks()
        
def display_tasks():
    global tasks
    print("\nThe Tasks Are: ")
    for index,i in enumerate(tasks, start=1):
        print(index,i.capitalize())
    print(" ")

#main 
tasks =[]
print("=====TO-DO List=====")
print("1.ADD A TASK\n2.DELETE / COMPLETED A TASK\n3.UPDATE A TASK\n4.DISPLAY ALL THE TASK\n5. EXIT\n")
while True:
    choice=int(input("Enter Your Choice: "))
    match choice:
        case 1:
            add_tasks()
        case 2:
            delete_tasks()
        case 3:
            update_tasks()
        case 4:
            display_tasks()
        case 5:
            print("Closing the Program...")
            break