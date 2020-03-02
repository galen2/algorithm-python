# 最短路径算法
# 从w[0][0] 到 w[n-1][n-1] 所经过的最短路径是多少
# 回溯算法实现方案的升级版
import sys
matrix = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7],[6, 8, 4, 3]]
n = 4
# 动态规划实现-- 动态转移表法
def minDistDP(matrix,n): 
    #初始化N*N的二位数组
    states = [0]*n
    for i in range(n):
     states[i] = [0]*n
    # 初始化states的第一行数据 
    sum = 0
    for j in range(n): 
        sum += matrix[0][j]
        states[0][j] = sum
    
    # 初始化states的第一列数据
    sum = 0
    for i in range(n): 
        sum += matrix[i][0]
        states[i][0] = sum
    # for循环：初始化其他行、列
    for i in range(1,n):
        for j in range(1,n):
            states[i][j] = matrix[i][j] + min(states[i][j-1], states[i-1][j])
    return states[n-1][n-1]
# minDist = minDistDP(matrix,n)
# print(minDist)



# 动态规划-动态转移方程法
#初始化N*N的二位数组
mem = [0] * n
for i in range(n) :
    mem[i] = [0] * n
def minDist(i,j):
    if(i == 0 and j ==0): 
        return matrix[0][0]
    if (mem[i][j] > 0) :
        return mem[i][j]
    minLeft = sys.maxsize
    if (j-1 >= 0): 
        minLeft = minDist(i, j-1)
    minUp = sys.maxsize
    if (i-1 >= 0) :
        minUp = minDist(i-1, j)

    currMinDist = matrix[i][j] + min(minLeft, minUp)
    mem[i][j] = currMinDist
    return currMinDist
minDist = minDist(n-1,n-1)
print(minDist)
