'''
    This module is just to demonstrate & test the OCR accuracy scripts.  Set
    file-name below.

    To just see tuple dump, set debug to False.
    To turn off f/s substitution, set FSCheck to False.
    To turn on end of line hyphen checks, add True after the debug
        variable when AccEval.GetScore() is called.
'''


import Dictionary
import FSBuilder
import AccEval

Filename = "data/wildirishgirl.txt"

debug = True

FSCheck = True

if debug:
    print("Verbose feedback enabled\n")

Lexicon = Dictionary.BuildLexicon(debug)

if FSCheck:
    FSSub = FSBuilder.BuildFS(Lexicon, debug)
else:
    FSSub = set()

with open(Filename, encoding='utf-8') as file:
    text = file.readlines()

print("Evaluating " + Filename)
Score = AccEval.GetScore(text,Lexicon,FSSub,debug)

print(Score)
