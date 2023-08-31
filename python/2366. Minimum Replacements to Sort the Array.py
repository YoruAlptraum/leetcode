from typing import List

def minimumReplacement(nums: List[int]) -> int:
    lnums = len(nums)
    if lnums == 0:
        return 0
    rep = 0
    prev = nums[lnums-1]
    for i in range(lnums-2,-1,-1):
        if nums[i] > prev:
            t = nums[i]//prev
            rep += t -1
            if nums[i] % prev != 0:
                rep += 1
            
            if nums[i] // 2 <= prev:
                nums[i] = nums[i] // 2
            else:
                nums[i] = nums[i] // t
        prev = nums[i]
    return rep

print('expected 20 |', minimumReplacement([1,13,15,2,5,14,12,17]))
print('expected  6 |', minimumReplacement([12,9,7,6]))
print('expected  2 |', minimumReplacement([3,9,3]))
print('expected  2 |', minimumReplacement([9,3]))
print('expected  2 |', minimumReplacement([9,4]))
print('expected  0 |', minimumReplacement([1,2,3,4,5]))
print('expected  0 |', minimumReplacement([1]))
