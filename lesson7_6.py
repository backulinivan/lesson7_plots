import matplotlib.pyplot as plt
import numpy as np


wordFile = open('input.txt','r')
words = wordFile.read().split()
lengths = [len(x) for x in words]
max_length = max(lengths)
gist_lengths = [0]*(max(lengths)+1)
for i in range(0, max_length+1):
    gist_lengths[i] = lengths.count(i)
gist_lengths = gist_lengths[1:]

y_pos = [1+i for i in range(max_length)]
plt.bar(y_pos, gist_lengths, align='center', alpha=0.8)
plt.xticks(y_pos, y_pos)
plt.ylabel('Value')
plt.title('Bar title')

plt.show()
