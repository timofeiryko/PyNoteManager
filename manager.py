import os, sys, importlib
from scripts.body_tools import *
from scripts.custom_tools import *
from scripts.config import *

dirname = os.path.dirname(__file__) + pathname


while True:
    command = input('Enter a command: ')
    if command not in command_dict:
        print('There is no such command! Try help')
        continue
    if command == 'quit':
        break
    if command == 'help':
        print(*command_dict.keys())
        continue
    exec(command_dict[command])

