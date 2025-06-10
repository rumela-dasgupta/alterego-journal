
# AlterEgo - Your Split Personality CLI Journal

AlterEgo is a command-line journal application that allows you to maintain different personas, each with its own set of journal entries. It's your digital split personality log!

---

## Features

- Add multiple personas (alter egos)
- Journal as different personas
- View past journal entries
- Simple and intuitive CLI-based interaction
- Stores data using JSON files

---

### 🔧 Requirements

- Python 3.7+
- Works on all platforms with a terminal

### Folder Structure

```
alterego/
├── alterego.py
├── data/
│   ├── personas.json          # Stores list of personas
│   └── journals/
│       └── <persona>.json     # Journal entries per persona
└── README.md
```

---

##Usage

Run the script with different flags:

### Add a Persona
```bash
python main.py --add-persona
```

### Add a Journal Entry
```bash
python main.py --add-entry
```

###View Journal (to be implemented)
```bash
python main.py --view-journal
```

### Switch Persona (placeholder)
```bash
python main.py --switch "PersonaName"
```

---

## Sample Entry Flow

1. Add a new persona with a name and description
2. Choose that persona to write a journal entry
3. Entries are timestamped and saved under `data/journals/<persona>.json`

---

## To Do

- [ ] Implement `--view-journal`
- [ ] Improve UX with better input handling
- [ ] Optional encryption for journal entries
- [ ] Export all entries to a single file (PDF/Markdown)

---

##License

This project is open-source and free to use for personal journaling and experiments.

