from typing import List

def runningSum(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [nums[0]] * n
    for i in range(1,n):
        res[i] = res[i-1] + nums[i]
    return res

if __name__ == "__main__":
    cases = [
        [[1,2,3,4], [1,3,6,10]],
        [[1,1,1,1,1], [1,2,3,4,5]],
        [[3,1,2,10,1], [3,4,6,16,17]]
    ]

    for c in cases:
        print(runningSum(c[0]) == c[1])