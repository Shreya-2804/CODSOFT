import os
tasks=[]
task=[]
index=0
new_task=[]


def Add_task(tasks,task):
    task= input("Enter a task: ")
    tasks.append(task)
    print("Tasks ",task," added to the list. ")


def Update_task(tasks,index,new_task):
    if tasks:
        index=int(input("Enter the task to update: "))
        if index <=len(tasks):
            new_task= input("Enter the updated task: ")
            tasks[index-1]=new_task
            print("Task updated successfully")
        else:
            print("Invalid task number")


def Delete_task(tasks,index):
    try:
        index= int(input("Enter task to delete: "))
        if 1<= index <= len(tasks):
            tasks.pop(index-1)
            print("Task ",index," has been removed.")
        else:
            print("task ",index," was not found.")

    except:
        print("Invalid input")


def Veiw_tasks(tasks):
    if not tasks:
        print("Currently there are no tasks.")
    else:
        print("tasks are:")
        for index,task in enumerate(tasks, start=1):
            print("task",index,".",task)



if __name__ == '__main__':
    print("To-do lists:")
    while True:
        print("\n")
        print("Select one of the following options:")
        print("1. Add a new task")
        print("2. Update an existing task")
        print("3. Delete a task")
        print("4. Veiw all tasks")
        print("5. Quit")

        choice= input("Enter your choice(1-5): ")
        if(choice=="1"):
            Add_task(tasks,task)
        elif(choice=="2"):
            Update_task(tasks,index,new_task)
        elif(choice=="3"):
            Delete_task(tasks,index)
        elif(choice=="4"):
            Veiw_tasks(tasks)
        elif(choice=="5"):
            print("Tasks saved.Exiting...")
            break
        else:
            print("Invalid input. Please try again.")










