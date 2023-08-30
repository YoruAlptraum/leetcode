from typing import List

def minimumReplacement(nums: List[int]) -> int:
    lnums = len(nums)
    if lnums == 0:
        return 0
    rep = 0
    prev = nums[lnums-1]
    for i in range(lnums-2,-1,-1):
        t = nums[i]/prev
        if nums[i] > prev:
            rep += t
        for i in t:
            nums[i] -= nums[i]%prev
        prev = nums[i]
    return rep

print('expected 6 |', minimumReplacement([12,9,7,6,17,19,21]))
print('expected 2 |', minimumReplacement([3,9,3]))
print('expected 2 |', minimumReplacement([9,3]))
print('expected 2 |', minimumReplacement([9,4]))
# print('expected 0 |', minimumReplacement([1,2,3,4,5]))
# print('expected 0 |', minimumReplacement([1]))
