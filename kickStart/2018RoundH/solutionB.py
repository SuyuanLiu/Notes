'''
2018.12.19
Problem:
一段长为N的墙壁，画家在上面作画，每一段对应一个分数，画家希望得分最高。
画家每天清晨作画，第一天可以任意选一段开始，后面必须在已作画片段相邻位置作画。
每天傍晚，由于洪水原因，将有一段墙壁被毁坏（已作画墙壁不会被破坏）。被毁坏的墙壁只能有一边相邻未破坏墙壁。（也就是说毁坏只会从两侧开始）。

Solution：
- 画家清晨作画，傍晚有墙壁被破坏，画家一共可以在 math.ceil(N/2) 段墙壁上作画；
- 由于被破坏墙壁只能从两侧开始，这题实际上是求连续 math.ceil(N/2) 个数值的最大值；

'''
import math 

def maxSum(num, cnt):
    max_sum = sum(num[0:cnt])
    pre_sum, cur_sum = sum(num[0:cnt]), 0

    for i in range(1, len(num) - cnt + 1):
        cur_sum = pre_sum - num[i-1] + num[i + cnt - 1]
        max_sum = max(max_sum, cur_sum)
        pre_sum = cur_sum
    
    return max_sum


def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        num = input()
        num = [int(num[i]) for i in range(len(num))]
        cnt = math.ceil(len(num) / 2)
        max_score = maxSum(num, cnt)
        
        print('Case #{}: {}'.format(i, max_score))




if __name__ == '__main__':
    main()