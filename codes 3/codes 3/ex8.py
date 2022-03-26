txt = 'A quick brown fox jumps over the lazy dog'
words = txt.split()
t = list()
print('Total words in line: ', len(words))
i = 1 
for w in words:
    t.append(words[-i])
    i = i + 1

print('reversed', t)
t.reverse()
print('reversed one more time',t)
t.sort()
print('sorted', t)
