import argparse
import json
import os
from datetime import datetime

parser=argparse.ArgumentParser(description="AlterEgo-Your Split personality journal")

# Add basic CLI arguments
parser.add_argument("--add-persona", action="store_true", help="Add a new alter ego")
parser.add_argument("--log", action="store_true", help="Log a journal entry")
parser.add_argument("--switch", type=str, help="Switch to a specific alter ego")
parser.add_argument('--add-entry', action='store_true', help='Add a journal entry to a persona')
parser.add_argument("--view-journal",action="store_true",help="View past journal entries")

#Reading the arguments
args=parser.parse_args()
#defining a function to be used later
def add_persona():
    print("You chose to add a new persona")
    name = input("Enter your Persona's name!: ")
    des = input("Enter a short description: ")
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/personas.json"):
        personas = []
    else:
        with open("data/personas.json", "r") as f:
            personas = json.load(f)
    new_persona = {"name": name, "description": des}
    personas.append(new_persona)
    with open("data/personas.json", "w") as f:
        json.dump(personas, f, indent=2)
    print(f"Persona '{name}' added successfully!")

#Testing what the user types
if args.add_persona:
    print("You chose to add a new persona")
    name=input("Enter you Persona's name!: ")
    des=input("Enter a short description: ")
    f=open("data/personas.json","r")
    personas=json.load(f) #[]
    f.close()
    new_persona = {"name": name, "description": des} #dictionary
    personas.append(new_persona) #appending in that list
    
    f=open("data/personas.json","w")
    json.dump(personas,f,indent=2)
    f.close()
    print(f"Persona '{name}' added successfully!")
elif args.add_entry: #manually pick a persona and write an entry
    print("You chose to add a journal entry")
    f=open("data/personas.json","r")
    personas=json.load(f)
    f.close()
    if not personas:
        print("No personas found.Please add one first")
        exit()
    #Displaying choices
    print("Which persona do you want to journal as?")
    for i, p in enumerate(personas): #shows existing persona (both index and the item)
        print(f"{i+1}. {p['name']} - {p['description']}") 
    choice = int(input("Enter choice number: ")) - 1
    selected = personas[choice]["name"]

    entry = input(f"What’s on your mind, {selected}? ")
    #Loading or creating the journal
    journal_path = f"data/journals/{selected}.json"
    os.makedirs("data/journals", exist_ok=True)
    if os.path.exists(journal_path):
        with open(journal_path, "r") as f:
            journal = json.load(f)
    else:
        journal = []
    # Add the new entry
    journal.append({
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "entry": entry
})
    f=open(journal_path,"w")
    json.dump(journal,f,indent=2)
    print(f"Journal Entry added for {selected}!")

elif args.view_journal:
    print("You chose to view journal entries")
    f=open("data/personas.json","r")
    personas=json.load(f)
    f.close()
    if not personas:
        print("No personas found.Please add one first")
        exit()
    for i, p in enumerate(personas): #shows existing persona (both index and the item)
        print(f"{i+1}. {p['name']} - {p['description']}") 
    choice = int(input("Enter choice number: ")) - 1
    selected = personas[choice]["name"]
    #Build the path to that persona's journal file
    journal_path = f"data/journals/{selected}.json"
    journal=[] #default empty list
    if os.path.exists(journal_path):
        with open(journal_path, "r") as f:
            journal = json.load(f)
    print(f"\nJournal entries for {selected}:")
    if not journal:
        print("No entries yet.")
    else:
        for entry in journal:
            print(f"- [{entry['timestamp']}] {entry['entry']}")
elif args.switch:
    name_to_switch = args.switch
    if not os.path.exists("data/personas.json"):
        print("No personas found.Please add one first")
        ch=input("Would you like to add a new persona first? (Y/N): ").strip().lower()
        if ch=="y":
            add_persona()
        elif ch=="n":
            print("No problem!Exiting..Have a great day ahead!")
            exit()
        else:
            print("Invalid input.Please check.")
            exit()
    f=open("data/personas.json","r")
    personas=json.load(f)
    f.close()
    if not personas:
        print("No personas available.")
        exit()
    print("Available personas:")
    for i, p in enumerate(personas):
        print(f"{i+1}. {p['name']} - {p['description']}")
    # Check if name_to_switch matches any persona name and making them lowercase for matching 
    # so that even if the user types in a different case it can still recognise the input persona
    match = None  # Assume no match at first
    for p in personas:
      if p["name"].lower() == name_to_switch.lower():
        match = p
        break  # Stop searching after the first match

    if not match:
        print(f"\n'{name_to_switch}' not found in the list.")
        ch = input("Would you like to select from the list instead? (Y/N): ").strip().lower()
        if ch == "y":
            try:
                choice = int(input("Enter your choice number: ")) - 1
                selected = personas[choice]["name"]
            except (IndexError, ValueError):
                print("Invalid choice. Exiting.")
                exit()
        else:
            print("Okay, exiting.")
            exit()
    else:
        selected = match["name"]

    # Save current persona
    with open("data/current.json", "w") as f:
        json.dump({"current": selected}, f)

    print(f"Switched to '{selected}' persona.")
elif args.log: #log as the currently switched persona, with no picking.
    print("Log an entry")
    if not os.path.exists("data/current.json"):
        print("No persona is currently active. Please switch to one using --switch.")
        exit()
    f=open("data/current.json","r")
    current=json.load(f)["current"]
    f.close()
    entry = input(f"What's on your mind, {current}? ")
    journal_path = f"data/journals/{current}.json"
    os.makedirs("data/journals", exist_ok=True)
    journal=[] #default empty list
    if os.path.exists(journal_path):
        with open(journal_path, "r") as f:
            journal = json.load(f)
    # Add the new entry
    journal.append({
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "entry": entry
})
    f=open(journal_path,"w")
    json.dump(journal,f,indent=2)
    print(f"Journal entry logged for '{current}'")

else:
    print("No valid option selected,use --help or --h")

