# PyNoteManager
This is a CLI for advanced management of your notes with simple commands.

To use this app, simpy clone this repo and place your notes into storage folder. You can set up the relative path and name of the folder with notes in **scripts/config.py**.

To manage your notes, just run **python manager.py**.

There are scripts which help to work with text in the files in the **scripts/body_tools.py**. You can add your own functions in the **scripts/custom_tools.py**. Don't forget to register it in the **config.py**! You are welcome to contribute new features :)

The list of commands:
- **help**: just prints the list of commands
- **quit**: stops the app
- **repl**: replaces the entered word to enother in a smart way: it takes punctuation into account, it isn't case sensetive. You can also delete some word from all your notes just skipping the "new word"

This list will expand as the application develops...
