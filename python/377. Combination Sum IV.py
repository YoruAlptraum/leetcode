from typing import List

def combinationSum4(nums: List[int], target: int) -> int:
    seen = {0:1}
    
    def combinations(target):
        if target in seen:
            return seen[target]
        n = 0
        for i in nums:
            if i <= target:
                n += combinations(target-i)
        seen[target] = n
        return n
    
    return combinations(target)
        

if __name__ == "__main__":
    print(combinationSum4(nums = [1,2,3], target = 0))
    print(combinationSum4(nums = [1,2,3], target = 1))
    print(combinationSum4(nums = [1,2,3], target = 2))
    print(combinationSum4(nums = [1,2,3], target = 3))
    print(combinationSum4(nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], target = 1))
