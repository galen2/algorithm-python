# 最短路径算法
# 从w[0][0] 到 w[n-1][n-1] 所经过的最短路径是多少
# 回溯算法：穷举所有的情况，然后对比得到最优解
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



def distDT(i,j,w,n):
    dist1 = w[i][j]
    dist1 = dist1 + w[i+1][j]
    dist1 = dist1 + w[i+1][j+1]

    dist2 = w[i][j]
    dist2 = dist2 + w[i][j+1]
    dist2 = dist2 + w[i+1][j+1]

    
    这个问题与分解之后的子问题，除了数据规模不同，求解思路完全一样