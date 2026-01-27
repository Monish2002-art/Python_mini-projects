#This is an To-Do-List_app in terminal - to add the list of works to be done

def do():
    options=["1.Add tasks","2.view tasks","3.delete tasks","4.exit"]

    for menu in options:
        print(menu)


tasks = []

while True:
    do()
    
    task=int(input("enter what to do: "))

    if task == 1:
        list = input("Lists = ")
        tasks.append(list)
        print("Task Added")

    elif task == 2:
        if len(tasks) == 0:
            print("None in tasks!! , please add !!")
        else:
            print("\nyour Tasks:")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}. {task}")
            print("-------------")
        
    elif task == 3:
        if len(tasks) == 0:
            print("!!!None to delete!!!")
        else:
            print("your tasks")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}. {task}")
            task_no = int(input("enter task to delete = "))
            deleted = tasks.pop(task_no -1)
            print("deleted task :", deleted)

    elif task == 4:
        print("!!!! ^_^ Thank you^_^ !!!!")
        break

    else:
        print("Invalid option")

