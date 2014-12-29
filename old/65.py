#!/usr/bin/env python
# 65 - Klingon Translator
import urllib2
from sys import argv

klingon = urllib2.quote(' '.join(argv[1:]))
site = 'http://klingon-translator.com/t.php?from=tlh&to=en&v=' + klingon
request = urllib2.Request(site, headers={'User-Agent': 'your mother'})
english = urllib2.urlopen(request).read()[:-1]

print english
