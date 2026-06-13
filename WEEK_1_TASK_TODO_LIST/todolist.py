tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in tasks:
                print("-", i)

    elif choice == "3":
        print("Program Closed")
        break

    else:
        print("Invalid Choice! Please try again.")