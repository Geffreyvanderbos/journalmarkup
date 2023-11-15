import os
import datetime

CONFIG_FILE = "config.txt"

def get_file_location():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as config_file:
            return config_file.readline().strip()

    file_location = input("Enter the path of your journal file: ")
    with open(CONFIG_FILE, "w") as config_file:
        config_file.write(file_location)
    return file_location

def add_newline_if_needed(file_location):
    with open(file_location, "r") as file:
        content = file.read()
    return not content.strip() or content[-1] != "\n"

def append_task(file_location):
    task_title = input("Enter the task title: ")
    newline = "\n" if add_newline_if_needed(file_location) else ""
    with open(file_location, "a") as file:
        file.write(f"{newline}- [ ] {task_title}\n")
    print("Task added successfully!")

def add_journal_entry(file_location):
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    newline = "\n\n" if add_newline_if_needed(file_location) else "\n"
    with open(file_location, "a") as file:
        file.write(f"{newline}{today_date}\n==========\n")
    print("New journal entry added successfully!")

def move_unfinished_tasks(file_location):
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    with open(file_location, "r") as file:
        content = file.readlines()

    unfinished_tasks = [task.strip() for task in content if task.strip().startswith("- [ ]")]

    if unfinished_tasks:
        content = [line for line in content if line.strip() not in unfinished_tasks]

        if f"{today_date}\n==========\n" not in content:
            content.append(f"\n\n{today_date}\n==========\n")

        content.extend([f"{task}\n" for task in unfinished_tasks])

        with open(file_location, "w") as file:
            file.writelines(content)

        print("Unfinished tasks moved to the new day.")
    else:
        print("No unfinished tasks to move.")

def add_meeting_template(file_location):
    newline = "\n" if add_newline_if_needed(file_location) else ""
    with open(file_location, "a") as file:
        file.write(f"{newline}> Meeting: \n> Atten: \n> Goals: \n> Notes: \n> Tasks: \n\n")
    print("Meeting template added successfully!")

def main():
    file_location = get_file_location()

    while True:
        print("\n1. Append a task")
        print("2. Add a new journal entry")
        print("3. Move unfinished tasks to a new day")
        print("4. Add a meeting template")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            append_task(file_location)
        elif choice == "2":
            add_journal_entry(file_location)
        elif choice == "3":
            move_unfinished_tasks(file_location)
        elif choice == "4":
            add_meeting_template(file_location)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
