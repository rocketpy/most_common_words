import re
import collections


with open('file_name.txt') as f:
text = f.read()

words = re.compile(r"a-zA-Z'").findall(text)
counts = collections.Counter(words)

print(counts.most_common(10)) 


#  one more example
from collections import Counter

with open('file_name.txt') as fin:
    counter = Counter(fin.read().strip().split())

print(counter.most_common())
