from typing import List
from collections import Counter

# easiest straight forward approach
def countKDifference(nums: List[int], k: int) -> int:
    ans = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if abs(nums[i]-nums[j]) == k:
                ans += 1
    return ans

def countKDifference2(nums: List[int], k: int) -> int:
    ans = 0
    dic = Counter(nums)
    for i in nums:
        x = i-k
        if x in dic:
            ans += dic[x]
    return ans

if __name__ == "__main__":
    cases = [
        [[1,2,2,1], 1],
        [[3,2,1,5,4], 2]
    ]

    for c in cases:
        print(countKDifference(c[0],c[1]), countKDifference2(c[0],c[1]))