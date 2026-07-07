tasks=[]

while True:
    print("/n============ TO DO LIST============")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice: (1-3) ")

    if choice == "1":
        tasks.append(input("Enter the task: "))
    elif choice == "2":
        print("*****Tasks:*****")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
