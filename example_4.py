import re
from collections import Counter


with open('file_name.txt') as file:
    passage = file.read()

words = re.findall(r'\w+', passage)
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)

# by steps
my_string = "Hello  world !,  Hi there !"
words = re.findall(r'\w+', my_string)  # words is a list with a words
# or lower
cap_words = [word.upper() for word in words] #capitalizes all the words
word_counts = Counter(cap_words) 


with open("file_name.txt") as f:
    text = f.read()

words = re.compile(r"[\w']+", re.U).findall(text)   # re.U == re.UNICODE
counts = collections.Counter(words)
