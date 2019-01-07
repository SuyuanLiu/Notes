'''
2018.12.18
Problem:
两个按钮（R，B），可以连续按N次，由R,B组成一个字符串。有p个前缀字符串，按钮按出的序列不能出现这P个前缀字符串。
问一共有多少种情况。

Solution：
- 如果P个前缀中包含'R', 'B'字符串，那么结果为0；
- def removeDup(S):其他情况：对P个前缀字符串检查，去掉重复作用的，比如'BB' 和 'BBRR'， 那么后一个子串可以被去掉；
- 用2^n减去不可以出现的情况，比如：某个不可以出现的字符串长度为a, 那么res = res - pow(2, n - a)

TODO:
def removeDup时间复杂度O(n^2),应该可以改进到O(n);
'''

def removeDup(S):
    idx_remove = set()
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if len(S[i]) <= len(S[j]) and S[i] == S[j][:len(S[i])]:
                idx_remove.add(j) 
    
    idx_remove = (list(idx_remove))
    idx_remove.sort()
    for i in idx_remove[::-1]:
        del S[i]

    return S 


def cal(forbid, N):
    res = pow(2, N)
    for i in range(len(forbid)):
        res = res - pow(2, N - len(forbid[i]))
    return res


def main():
    t = int(input())
    for i in range(1, t + 1):
        n, p = [int(s) for s in input().split(' ')]
        forbid_B, forbid_R = [], []
        for j in range(p):
            s = input()
            if s[0] == 'B':
                forbid_B.append(s)
            else:
                forbid_R.append(s)
        forbid_B.sort()
        forbid_R.sort()
        if forbid_B and forbid_R and forbid_B[0] == 'B' and forbid_R[0] == 'R':
            res = 0
        else:
            forbid_B = removeDup(forbid_B)
            forbid_R = removeDup(forbid_R)
            res = cal(forbid_B + forbid_R, n)

        print('Case #{}: {}'.format(i, res))


if __name__ == '__main__':
    main()



