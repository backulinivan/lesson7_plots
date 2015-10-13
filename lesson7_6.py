import numpy as np
import matplotlib.pyplot as plt

strfile = open('input.txt', 'r')
def fileWordlengthCount(f):
    count = 0
    lengthsArr = []
    strArr = f.readlines()
    for i in range(len(strArr)):
        for j in range(len(strArr[i])):
            if strArr[i][j] != ' ' or strArr[i][j] != '\n':
                count += 1
            else:
                lengthsArr.append(count)
                count = 0    
    return(lengthsArr)            

objects = fileWordlengthCount(strfile)
y_pos = np.arange(1, 20, 1)
partArr = []
for i in range(1, 20, 1):
    partArr[i] = objects.count(i)/20
performance = partArr

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.ylabel('Доля')
plt.title('Длина слов')

plt.show()
