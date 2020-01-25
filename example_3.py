import re
import collections


words = re.findall(r'\w+', open(file_name.txt).read().lower() )
most_common_words = collections.Counter(words).most_common(20)  #  20 - words

print(most_common_words)
