'''
    This module accepts an already constructed lexicon and creates a set of
    words with all non-final esses replaced with effes.  This module can be used
    to evaluate OCR accuracy if run after Dictionary is loaded or used to clean
    OCR by providing a dictionary for subsitutions.

    BuildFS: returns a set of words with f/s substituted
    DictFS: returns a dictionary with f/s subsitutions that refer to originals
    
'''

## This function is built into Acc

def BuildFS(Lexicon, verbose=False):

    FSRules = set()

    if verbose:
        print("Building F/S Rules")

    for word in Lexicon:
        if 's' in word and word.endswith('s') and word.count('s') == 1:
            continue
        elif 's' in word and word.endswith('ss') and word.count('s') == 2:
            continue
        elif 's' in word and word.endswith('s'):
            num = word.count('s') - 1
            if word.endswith('ss'):
                num = num - 1
            FSRules.add(word.replace('s','f',num))
        elif 's' in word:
            FSRules.add(word.replace('s','f'))

    if verbose:
        print(str(len(FSRules)) + " rules created\n")

    return FSRules

def DictFS(Lexicon, verbose=False):

    FSRules = dict()

    if verbose:
        print("Building F/S Rules")

    for word in Lexicon:
        if 's' in word and word.endswith('s') and word.count('s') == 1:
            continue
        elif 's' in word and word.endswith('ss') and word.count('s') == 2:
            continue
        elif 's' in word and word.endswith('s'):
            num = word.count('s') - 1
            if word.endswith('ss'):
                num = num - 1
            FSRules[word.replace('s','f',num)] = word
        elif 's' in word:
            FSRules[word.replace('s','f')] = word

    if verbose:
        print(str(len(FSRules)) + " rules created\n")

    return FSRules
