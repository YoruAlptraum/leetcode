from typing import List

def leftRightDifference(nums: List[int]) -> List[int]:
    n = len(nums)
    r, racc = [0]*n, 0
    l, lacc = [0]*n, 0
    
    for i in range(n):
        r[i] += racc
        l[-i-1] += lacc
        racc += nums[i]
        lacc += nums[-i-1]

    for i in range(n):
        l[i] = abs(l[i] - r[i])
    return l

if __name__ == '__main__':
    cases = [
        [[10,4,8,3],[15,1,11,22]],
        [[1],[0]]
    ]

    for c in cases:
        print('passed' if leftRightDifference(c[0])==c[1] else 'failed')
