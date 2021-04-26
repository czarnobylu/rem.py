This is a reminder/todo list organizer written in python.

Dependencies: glob

Usage:
1. Create a ~/.todo directory
2. Launch the script with -a flag and the name of the note after, eg: 
```bash
rem.py -a My First Note
```
It will launch your configured editor so you can input the content of the note.

3. You can remove notes with -r flag like so:
```bash
rem.py -r My First Note
```
This will use rm to remove the file from $HOME/.todo directory.