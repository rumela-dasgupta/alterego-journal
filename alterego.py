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
elif args.add_entry:
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


elif args.log:
    print("Log an entry")
elif args.switch:
    print(f"Switching to persona: {args.switch}")
else:
    print("No valid option selected")

