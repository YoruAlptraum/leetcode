from typing import List
from collections import Counter
from math import comb

def numIdenticalPairs(nums: List[int]) -> int:
    good = 0
    seen = {}
    for i in nums:
        if i in seen:
            good+=seen[i]
            seen[i] +=1
        else:
            seen[i] = 1
    return good

def numIdenticalPairsWithMath(nums: List[int]) -> int:
    # comb will show the number of pairs in i 
    # counter(nums).values() will return a list of the count of each value
    # the values do not matter anymore since all we care about for this problem is the number of pairs for each number with itself
    return sum([comb(i,2) for i in Counter(nums).values()])

if __name__ == "__main__":
    cases = [
        [[1,2,3,1,1,3],4],
        [[1,1,1,1],6],
        [[1,2,3],0]
    ]
    for c in cases:
        print(numIdenticalPairsWithMath(c[0]),'|',c[1])
