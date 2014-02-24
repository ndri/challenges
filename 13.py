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

total = sum([ord(i) for i in question])
    
print answers[total%len(answers)]
