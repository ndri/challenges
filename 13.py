#!/usr/bin/env python
# 13 - Magic Eight Ball
from sys import argv

question = ' '.join(argv[1:])
answers = [
'Sure. Why not?',
'Definitely.',
'Absolutely.',
'Certainly.',
'No doubt about it.',
'It\'s a well known fact.',
'Indubitably.',
'I guess so.',
'Indeed.',
'I guess not.',
'Not really.',
'Not at all.',
'The answer is no.',
'Absolutely not.',
'Why would you even consider that?',
'Nope.',
]

total = 0
for letter in question:
    total += ord(letter)
    
print answers[total%len(answers)]
