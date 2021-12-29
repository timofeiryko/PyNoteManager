import os, sys
import re, string
from .config import *

def replace_word(to_delete, to_print, word_list, punct):
    
    replace_dict = {
        to_delete: to_print,
        to_delete.capitalize(): to_print.capitalize(),
        to_delete.upper(): to_print.upper() 
    }
     
    out_list = []
    modified = False
    capitalize_next = False
    
    for raw_word in word_list:
        #Separate punctuation
        #Use custom variable punct, not string.punctuation, because we don't want to remove #, $, %, @
        endings = ('!', '.', '?', '...')
        #Make "cleared" word without punctuation
        word = raw_word.translate(str.maketrans('', '', punct))                        
        if word not in replace_dict:
            out_list.append(raw_word)
        else:
            modified = True
            new_word = replace_dict[word]
            if capitalize_next and new_word == new_word.lower():
                new_word = new_word.capitalize()
            #New el is new word with original punctuation
            if new_word != '':
                new_el = raw_word.replace(word, new_word)
                out_list.append(new_el)
            #We don't want to delete ending markers like . ! ? ...
            elif raw_word.endswith(endings):
                for suffix in endings:
                    if raw_word.endswith(suffix):
                        end = suffix
                if len(out_list) >= 1:
                    if not out_list[-1].endswith(endings):
                        if len(out_list) >= 2 and out_list[-1] in ['—', '-']:
                            out_list[-2] += end
                            out_list.pop(-1)
                        else:
                            out_list[-1] += end
                capitalize_next = True
    return out_list, modified


def replace_word_in_dir(dirname, textformats):
    
    os.chdir(dirname)
    print_modified = False
    
    to_delete = input('The word to be replaced: ').lower()
    to_print = input('New word: ').lower()  
    
    for filename in os.listdir(dirname):
        if filename.endswith(textformats):
            #Create tmp file to be sure that it exists (usefull when we work with empty file)
            tmpfile = open(filename+'.tmp', 'a+')
            tmpfile.close()
            for line in open(filename, 'r'):
                with open(filename + '.tmp', 'a+') as output:
                    word_list = line.split()
                    out_list, print_modified = replace_word(to_delete, to_print, word_list, punct)
                    outline = ' '.join(out_list) + '\n'
                    output.write(outline)
            
            os.rename(filename + '.tmp', filename)
        if print_modified:
            print(filename + ' was modified!')
    
    print('Replacement done!')

# test_str = "I want to delete 'this' text? Text! Okay, let's go"
# to_delete = 'text'
# to_print = ''

# test_input = (to_delete, to_print, test_str.split(), punct)
# print(replace_word(*test_input))