import matplotlib.pyplot as plt
import numpy as np


input=open('input.txt','r')
date=input.read().split()
date_len=[len(x) for x in date]
max_len=max(date_len)
gist_date=[0]*max_len
for x in date_len:
    gist_date[x-1]+=1

y_pos = [1+i for i in range(max_len)]
plt.bar(y_pos, gist_date, align='center', alpha=0.8)
plt.xticks(y_pos, y_pos)
plt.ylabel('Value')
plt.title('Bar title')

plt.show()
