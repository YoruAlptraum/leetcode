from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            return [i,dic[nums[i]]]
        dic[target-nums[i]] = i

print(twoSum(nums = [2,7,11,15], target = 9))