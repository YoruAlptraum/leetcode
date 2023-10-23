from typing import List

# first attempt to use 2 pointers
def countPairs(nums: List[int], target: int) -> int:        
    pairs = 0
    i,j = 0,1
    n = len(nums)
    while i < n-1:
        if nums[i] + nums[j] < target:
            pairs+=1
        j += 1
        if j >= n:
            i += 1
            j = i + 1
    return pairs

# using pointers with sliding window 
def countPairs2(nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    l, r = 0, n-1
    pairs = 0
    while l < r:
        if nums[l] + nums[r] < target:
            pairs += r-l
            l += 1
        else:
            r -= 1
    return pairs

if __name__ == "__main__":
    cases = [
        [[-1,1,2,3,1], 2, 3],
        [[-6,2,5,-2,-7,-1,3], -2, 10]
    ]

    for case in cases:
        print(countPairs2(case[0],case[1]),'|',countPairs(case[0],case[1]))
