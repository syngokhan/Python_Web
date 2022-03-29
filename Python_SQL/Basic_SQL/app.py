from database import create_table,add_entry,get_entries

menu = """Please select one of the following options:
    1) Add new entry for today.
    2) View Entries.
    3) Exit.

    Your Selection : """

welcome = "Welcome to the programming diary!"

def prompt_new_entry():
    entry_content = input("What have you learned today?\n")
    entry_date = input("Ender the date :\n")
    add_entry(entry_content,entry_date)

def view_entries(entries):

    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


print(welcome)
create_table()

while True:
    value = input(menu) 

    if value == "1":
        print("Adding Function n\n")

        prompt_new_entry()

    elif value == "2":
        print("Viewing...\n\n")
        
        entries = get_entries()
        view_entries(entries)

    elif value == "3":
        print("Quit.")
        break

    else:
        print("Invalid option, please try again!")