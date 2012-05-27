'''
    This module is just to demonstrate & test the OCR accuracy scripts.  Set
    file-name below.

    To just see score, set debug to False.
    To turn off f/s substitution, set FSCheck to False.
    To turn on end of line hyphen checks, set CheckHyphen to True
'''


import Dictionary
import FSBuilder
import LowerEval

Filename = "data/wildirishgirl.txt"

debug = True

FSCheck = True

CheckHyphen = False

if debug:
    print("Verbose feedback enabled\n")

Lexicon = Dictionary.BuildLexicon(debug)

if FSCheck:
    FSSub = FSBuilder.BuildFS(Lexicon, debug)
else:
    FSSub = set()

with open(Filename, encoding='utf-8') as file:
    text = file.readlines()

print("Evaluating " + Filename + " after forcing all lower-case")
Score = LowerEval.GetScore(text,Lexicon,FSSub,debug,CheckHyphen)

print(Score)

print("Base accuracy: " + str(Score[1]/Score[0]))
print("Adjusted accuracy: " + str((Score[1] + Score[2])/Score[0]))
