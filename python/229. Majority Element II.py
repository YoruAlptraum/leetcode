from typing import List
from collections import Counter

def majorityElement(nums: List[int]) -> List[int]:
    count = {}
    res = set()
    t = len(nums)//3
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        if count[i] > t:
            res.add(i)
    return list(res)

def majorityElementWithCounter(nums: List[int]) -> List[int]:
    count = Counter(nums)
    t = len(nums)//3
    ans = []
    for c, i in count.items():
        if i > t:
            ans.append(c)
    return ans

if __name__ == "__main__":
    cases = [
        [[3,2,3],[3]],
        [[1],[1]],
        [[1,2],[1,2]]
    ]
    for c in cases:
        print(majorityElementWithCounter(c[0]),'|',c[1])