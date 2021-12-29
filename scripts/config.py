# Enter the relative path from manage.py to the folder where you keep your notes
pathname = '/storage'

# Set up the fromats that are used for taking notes. Do not forgot the dot!
# .tmp is prohibited, because it is used for temorary files!
textformats = ('.md', '.txt')

# Set up a set of characters that are recognized as punctuation marks in repl tool
punct = '!"&\'()*+,./:;<=>?[\\]^_`{|}~'
# By default, #$%@ are not considered unlike in the string.punctuation

# You can rename the tools as you wish and register new custom features
# Commands "help" and "quit" can not be changed
# Keys are commands that are inputed and values are functions that should be executed
command_dict = {
    'help': 'RESERVED',
    'quit': 'RESERVED',
    'repl': 'replace_word_in_dir(dirname, textformats)'
    
}
# You are welcome to contribute new features!
