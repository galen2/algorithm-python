# 最短路径算法
# 从w[0][0] 到 w[n-1][n-1] 所经过的最短路径是多少

import sys
minDist = sys.maxsize
w = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7],[6, 8, 4, 3]]
#w = [[1, 3, 5], [2, 1, 3], [5, 2, 6]]

# 回溯算法实现
def minDistBT(i, j, dist, w, n):
    global minDist
    if (i == n and j == n):
        if (dist < minDist):
            minDist = dist
            return
    if (i < n):  # 往下走，更新i=i+1, j=j
        minDistBT(i + 1, j, dist+w[i][j], w, n)
    
    if (j < n): # 往右走，更新i=i, j=j+1
        minDistBT(i, j+1, dist+w[i][j], w, n)
# minDistBT(0,0,0,w,3)
# print(minDist)
