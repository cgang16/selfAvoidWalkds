import numpy as np 
import os 
import time

sn = 4
flags = None 

# (x, y) current pos
# m steps taken
def walksFrom(m, x, y):
    global sn, flags
    m1 = m + 1
    if m1 == sn:
        return flags[x + 1][y] + flags[x][y + 1] + flags[x - 1][y] + flags[x][y - 1]
    
    count = 0
    
    def incCount(m, x, y):
        count = 0
        if flags[x][y]:
            flags[x][y] = False
            count = walksFrom(m, x, y)
            flags[x][y] = True
        return count
    
    x = x + 1
    count += incCount(m1, x, y)
    x = x - 2
    count += incCount(m1, x, y)
    x = x + 1
    y = y + 1
    count += incCount(m1, x, y)
    y = y - 2 
    count += incCount(m1, x, y)
    return count 
    
        
def countDifferentRoutes(n):
    global sn, flags
    sn = n
    flags = np.zeros((64, 64), dtype=np.int32)
    for i in range(64):
        for j in range(64):
            flags[i][j] = (i > 0 and j > 0)
    flags[1][1] = 0
    flags[2][1] = 0
    return walksFrom(1, 2, 1)

def main():
    start = time.time()
    print(countDifferentRoutes(20))
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()