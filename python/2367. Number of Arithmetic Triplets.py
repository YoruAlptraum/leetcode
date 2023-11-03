from typing import List

def arithmeticTriplets(nums: List[int], diff: int) -> int:
    map = [0] * len(nums)
    ans = 0
    for i in range(len(nums)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if nums[i] - nums[j] == diff:
                ans += map[i]
                map[j] += 1
    return ans

if __name__ == "__main__":
    cases = [
        [[0,1,4,6,7,10], 3, 2],
        [[4,5,6,7,8,9], 2, 2]
    ]

    for case in cases:
        print(arithmeticTriplets(case[0],case[1]) == case[2])
