'''
    This module is just to demonstrate & test the OCR accuracy scripts.  Set
    data directory below.  If you set this script to check for F/S, final
    report will provide both the adjusted score and the base score.

    To just see score report, set debug to False.
    To turn off f/s substitution, set FSCheck to False.
    To turn on end of line hyphen checks, add True after the debug
        variable when AccEval.GetScore() is called
'''

import Dictionary
import FSBuilder
import AccEval
import glob

DataDirectory = "data/"

debug = True

FSCheck = True

if debug:
    print("Verbose feedback enabled\n")

Lexicon = Dictionary.BuildLexicon(debug)

if FSCheck:
    FSSub = FSBuilder.BuildFS(Lexicon,debug)
else:
    FSSub = set()

report = list()

if debug:
    print("Building file list from " + DataDirectory)

TextList = glob.glob(DataDirectory + "*.txt")

print("Preparing score report for " + str(len(TextList) ) + " items in " + DataDirectory + "\n")

for Filename in TextList:
    if debug:
        print("Evaluating " + Filename)        

    with open(Filename, encoding='utf-8') as file:
        text = file.readlines()

    Score = AccEval.GetScore(text,Lexicon,FSSub,debug)

    report.append((Filename,Score))

print("Batch Accuracy Report:")
print("Accuracies for lower-case only and captialized + lower-case")

if len(FSSub) > 0:
    print("Scores adjusted according to F/S substitution rules")
else:
    print("F/S substitution rules were not used in this report")

print("\nFile\t\tLowAcc\t\tCap+LowAcc\tWithoutFSsubs")
for result in report:
    name = result[0].replace(DataDirectory,'')
    if len(name) > 10:
        name = name[:12]
    acc = (result[1][4] + result[1][5]) / result[1][3]
    adjnum = result[1][1] + result[1][2] + result[1][4] + result[1][5]
    adjden = result[1][0] + result[1][3]
    nosub = (result[1][1] + result[1][4]) / adjden
    print(name + ":\t" + str(acc)[:8] + "\t" + str(adjnum/adjden)[:8] + "\t" + str(nosub)[:8])
