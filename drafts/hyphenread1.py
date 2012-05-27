'''
    This module reads in the specified text file and cleans it for use with
    accuracy and analytical modules.  It returns the "cleaned" file as a list.

    TODO: Allow it to accept commands as far as cleaning rules go
'''

Punctuation = '.,():;"!?•$%@#<>+-—=/[]*^\'{}_■~\\|«»©&~`£·'

## Reads in file, stores as list, makes minimal corrections.

def CleanText(FileName, Lexicon, debug=False):

    if debug:
        print("Reading " + FileName)

    with open(FileName, encoding='utf-8') as file:
        text = file.readlines()

    words = list()
    
    if debug:
        print("Cleaning " + FileName)

    for line in text:
        line = line.rstrip()
        line = line.lower()
        line = line.replace(',',' ')
        words.extend(line.split())

## First pass, strips punctuation from beginning/ending of words & sets all
## characters to lower-case to match lexicon.  Ignores digits and empty spots.
## NOTE: Commas removed above to account for numbers greater than 999.

    cleanwords = list()
    tryfuse = str()
    corrected = 0

    for f in words:

## This checks for possible end of line fusion.

        if f.endswith('-') or f.endswith('—'):
            f = f.strip(Punctuation)
            if f.isdigit() == False and len(f) >= 1:
                tryfuse = f
            continue

        f = f.strip(Punctuation)

        if len(f) < 1:
            continue

        if f.isdigit():
            continue

## Current checks to see if fusion will result in a word before doing so.
## Need to consult with Ted about this!

        if tryfuse != str():
            if tryfuse + f in Lexicon:
                cleanwords.append(tryfuse + f)
                corrected = corrected + 1
                tryfuse = str()
                continue
            elif tryfuse.isdigit() == False and len(tryfuse) >= 1: 
                cleanwords.append(tryfuse)
            tryfuse = str()

        cleanwords.append(f)

    if debug:
        print(str(len(cleanwords)) + " tokens processed")
        print(str(corrected) + " words at end of line corrected")
        print("Finished " + FileName + "\n")

    return cleanwords
