todolist=[] #list to add and remove stuff
def add_task():
    try:
        addtask=input("Enter the task that need to be added: ")
        todolist.append({"Task":addtask, "Status": "Pending"})
        print("Task added")
    except ValueError:
        print("Enter valid choice1")
def list_task():
    try:
        if len(todolist) == 0:
            print("No pending tasks/no tasks added")
        else:
            for index, addtask in enumerate(todolist, 1):
                print(f" {index}. {addtask['Task']}- {addtask['Status']}")
    except ValueError:
        print("Enter valid choice")
def delete_task():
    if len(todolist) == 0:
        print("No pending tasks to be deleted")
    else:
        try:
            indextoberemoved= int(input('enter the number of the task to be removed: '))-1
            if 0<= indextoberemoved <len(todolist):
                removed_task=todolist.pop(indextoberemoved)
                print(f"Task removed: {removed_task}")
            else:
                print('enter correct option')
        except ValueError:
            print("Enter a Valid choice")
def update_task():
    if len(todolist) == 0:
        print("No pending tasks to be updated")
    else:
        try:
            indextobeupdated= int(input('enter the number of the task to be updated: '))-1
            if 0<= indextobeupdated <len(todolist):
                todolist[indextobeupdated]['Status' ]='done'
                print(f"The task {todolist[indextobeupdated]['Task'] } has been marked as done")
            else:
                print('enter correct option')
        except ValueError:
            print("Enter a Valid choice")
def exit_task():
    print("Exiting....")
    exit()



def menu():
    while True:
        print("     Menu    ")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Mark as completed")
        print("5. Exit")
        try:
            choice=int(input("Enter your choice: "))

            if choice==1:
                add_task()
            elif choice==2:
                list_task()
            elif choice==3:
                delete_task()
            elif choice==4:
                update_task()
            elif choice==5:
                exit_task()
            else:
                print("Invalid Choice! Enter a valid one")
        except ValueError:
            print("Enter a Valid choice")

menu()