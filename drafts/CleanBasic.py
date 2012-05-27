'''
    This module reads in the specified text file and cleans it for use with
    accuracy and analytical modules.  It returns the "cleaned" file as a list.

    TODO: Allow it to accept commands as far as cleaning rules go
'''

Punctuation = '.,():-—;"!?•$%@#<>+=/[]*^\'{}_■~\\|«»©&~`£·'

## -—

## Reads in file, stores as list, makes minimal corrections.

def CleanText(FileName, verbose=False):

    if verbose:
        print("Reading " + FileName)

    with open(FileName, encoding='utf-8') as file:
        text = file.readlines()
        words = list()
        for line in text:
            line = line.rstrip()
            line = line.replace(',',' ')
            words.extend(line.split())

## First pass, strips punctuation from beginning/ending of words & sets all
## characters to lower-case to match lexicon.  Ignores digits and empty spots.
## NOTE: Commas removed above to account for numbers greater than 999.

    if verbose:
        print("Cleaning " + FileName)

    cleanwords = list()

    for f in words:
        f = f.strip(Punctuation)
        f = f.lower()
        if len(f) < 1:
            continue
        if f.isdigit():
            continue
        cleanwords.append(f)

    if verbose:
        print(str(len(cleanwords)) + " tokens processed\n")

    return cleanwords

if __name__ == '__main__':
    test = CleanText("MarrFPJ.txt", True)
    for word in test:
        print(word)
