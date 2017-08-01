from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under']

word_counts = Counter(words)
top_three = word_counts.most_common(4)
endswt = [name for name in words if name.endswith(('s', 'k'))]
print endswt
print(top_three)
print(word_counts)