import Dictionary
import ReadText
import hyphenread1
import hyphenread2
import FSBuilder

Lexicon = Dictionary.BuildLexicon(True)

FSSub = FSBuilder.BuildFS(Lexicon, True)

## Text = ReadText.CleanText("AustBCR.txt", True)
Text = hyphenread1.CleanText("AustBCR.txt", Lexicon, True)

Match = 0

Sub = 0

Miss = set()

for word in Text:
    if word in Lexicon:
        Match = Match + 1
        continue
    elif word in FSSub:
        Match = Match + 1
        Sub = Sub + 1
        continue

print("Base Matches: " + str(Match - Sub))
print("Sub. Matches: " + str(Sub))
print("Total Matches: " + str(Match) + "\n")

print("Base Accuracy: " + str((Match - Sub) / len(Text)))
print("Final Accuracy: " + str((Match / len(Text))))
print("Correction: " + str((Match / len(Text)) - ((Match - Sub) / len(Text))))

## Test = FSBuilder.DictFS(Lexicon,True)

## print(Test)
