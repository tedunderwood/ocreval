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
    
    if debug:
        print("Cleaning " + FileName)

    cleanwords = list()
    fuse = str()
    corrected = 0
    burp = False

    for line in text:
        line = line.rstrip()
        line = line.lower()
        line = line.replace(',',' ')

        words = line.split()

        if fuse != str() and len(words) > 1:
            print(words[0])
            words[0] = words[0].strip(Punctuation)
            words[0] = fuse + words[0]
            fuse = str()
            cleanwords.append(words[0])
            if burp:
                print("Corrected: " + words[0])
                burp = False
            del words[0]
            corrected = corrected + 1
        elif fuse != str():
            print(fuse)
            burp = True
            continue
            ##print(fuse)
            ##fuse = str()

        if line.endswith('-') or line.endswith('—'):
            fuse = words.pop()
            fuse = fuse.strip(Punctuation)
            if fuse.isdigit():
                fuse = str()
            
        for w in words:
            w = w.strip(Punctuation)
            if w.isdigit():
                continue
            if len(w) < 1:
                continue
            cleanwords.append(w)

    if debug:
        print(str(corrected) + " words at end of line corrected")
        print("Finished " + FileName + "\n")

    return cleanwords
