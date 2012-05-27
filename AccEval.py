'''
    This module evaluates the accuracy of an OCR text.  It accepts, at minimum,
    the text as a list of lines and the dictionary used for evaluation.  It
    also accepts special rule sets (ie, F/S substitution) but will still
    score a text if none is passed in.  If specified, will process tokens
    generated using end of line hyphen fusing.

    Requires: List of lines, processed dictionary.
    Optional: Substitution rules, vebose flag, hyphen flag

    Module returns a tuple of 6 length: total number of capitalized tokens,
    total number of capitalized dictionary matches, total number of capitalized
    matches through subsitution, total number of lower-case tokens, total
    number of lower-case dictionary matches, and total number of lower-case
    matches through substitution.
'''


import TokenGen

def GetScore(Text,Lexicon,Rules=set(),verbose=False,hyphen=False):

    CapsMatch = 0
    CapsSub = 0
    CapsCount = 0

    LowMatch = 0
    LowSub = 0
    LowCount = 0
    
    if verbose:
        print("Attempting token matching")
        if Rules == set():
            print("No substitution rules loaded")

## If not asked to check for possible fragmented matches, use basic checker.
## Function will default to basic checker.

    if hyphen == False:
        Tokens = TokenGen.Basic(Text,verbose)
    else:
        Tokens = TokenGen.Hyphen(Text,Lexicon,Rules,verbose)

## Maintains separate scores for substitution if rules were passed in, as well
## as separate scores for capitals, lowercase. Note that tokens like
## "wiU" (will) are not counted as capitalized.

    for word in Tokens:
        LowerWord = word.lower()
        if word[0].islower():
            LowCount = LowCount + 1
            if LowerWord in Lexicon:
                LowMatch = LowMatch + 1
            elif len(Rules) >= 1 and LowerWord in Rules:
                LowSub = LowSub + 1                
        else:
            CapsCount = CapsCount + 1
            if LowerWord in Lexicon:
                CapsMatch = CapsMatch + 1
            elif len(Rules) >= 1 and LowerWord in Rules:
                CapsSub = CapsSub + 1

    if verbose:
        print("\t" + str(CapsCount) + " total capitalized tokens")
        print("\t" + str(CapsMatch) + " total capitalized dictionary matches")
        print("\t" + str(CapsSub) + " total capitalized valid substitutions")
        print("\t" + str(LowCount) + " total lower-case tokens")
        print("\t" + str(LowMatch) + " total lower-case dictionary matches")
        print("\t" + str(LowSub) + " total lower-case valid substitutions\n")

## Return the six scores as a tuple.

    return (CapsCount,CapsMatch,CapsSub,LowCount,LowMatch,LowSub)
