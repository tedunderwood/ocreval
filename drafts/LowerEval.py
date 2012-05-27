'''
    This module evaluates the accuracy of an OCR text.  It accepts, at minimum,
    the text as a list of lines and the dictionary used for evaluation.  It
    also accepts special rule sets (ie, F/S substitution) but will still
    score a text if none is passed in.  If specified, will process tokens
    generated using end of line hyphen fusing.

    Requires: List of lines, processed dictionary.
    Optional: Substitution rules, vebose flag, hyphen flag

    Module returns a tuple of 2 length.  Index 0 will always return accuracy
    calculated using the total number of matched tokens.  If substitution
    rules are passed into the function, then Index 1 will return a base
    accuracy score that ignores matches resulting from substitution.  If no
    rules are passed into function, Index 1 will be the same as Index 0.
'''


import LowerGen

def GetScore(Text,Lexicon,Rules=set(),verbose=False,hyphen=False):

    Match = 0
    Sub = 0
    
    if verbose:
        print("Attempting token matching")
        if Rules == set():
            print("No substitution rules loaded")

## If not asked to check for possible fragmented matches, use basic checker.
## Function will default to basic checker.

    if hyphen == False:
        Tokens = LowerGen.Basic(Text,verbose)
    else:
        Tokens = LowerGen.Hyphen(Text,Lexicon,Rules,verbose)

## Maintains separate scores for substitution if rules were passed in, as well
## as separate scores for capitals, lowercase

    for word in Tokens:
        if word in Lexicon:
            Match = Match + 1
        elif len(Rules) >= 1 and word in Rules:
            Sub = Sub + 1                

    if verbose:
        print("\t" + str(len(Tokens)) + " total tokens")
        print("\t" + str(Match) + " total dictionary matches")
        print("\t" + str(Sub) + " total valid substitutions")

## Return the six scores as a tuple.

    return (len(Tokens),Match,Sub)
