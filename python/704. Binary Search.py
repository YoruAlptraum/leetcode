from typing import List
import bisect

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        needle = (l+r) // 2
        num = nums[needle]
        if num == target:
            return needle
        if num > target:
            r = needle
        else:
            l = needle +1
    return -1

# both pointers inclusive
def search2(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        num = nums[mid]
        if num == target:
            return mid
        if target < num:
            r = mid -1
        else:
            l = mid +1
    return -1

print(search(nums = [-1,0,3,5,9,12], target = 9)) # expected 4
print(search(nums = [-1,0,3,5,9,12], target = 2)) # expected -1
print(search2(nums = [-1,0,3,5,9,12], target = 9)) # expected 4
print(search2(nums = [-1,0,3,5,9,12], target = 2)) # expected -1
print(bisect.bisect_left([-1,0,3,5,9,12], 2))