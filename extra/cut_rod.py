
def Modify_Cut_rod(p:list, n:int, c: int):
    """
    p: price list, 不同长度对应的价格
    n: 长度
    c: 每次切除的cost
  	返回最优的切法和价格
    """
    r = [0]*n  # 存某个长度的最优解
    solution = []  # 切法
    for i in range(n):
        q = p[i]
        for j in range(i):
            tp = p[j]+r[i-j-1]-c
            if tp > q:
                solution.append(j)
                q = tp
        r[i] = q
    return r[-1], solution



if __name__ == "__main__":
    p = [1, 20, 33, 36]
    print(Modify_Cut_rod(p, 4, 1))
    print(Modify_Cut_rod(p, 4, 2))