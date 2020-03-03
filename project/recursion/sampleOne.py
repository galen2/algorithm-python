#假如这里有 n 个台阶，每次你可以跨 1 个台阶或者 2 个台阶，请问走这 n 个台阶有多少种走法？如果有 7 个台阶，你可以 2，2，2，1 这样子上去，也可以 1，2，1，1，2 这样子上去，
#总之走法有很多，那如何用编程求得总共有多少种走法呢？

def steps(n):
    if (n == 1):
        return 1
    if (n == 2):
        return 2
    return steps(n-1)+steps(n-2)
num = steps(4)
print(num)