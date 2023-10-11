# WIP

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

if __name__ == "__main__":
    cases = [
        [[1,13,15,2,5,14,12,17],20],
        [[12,9,7,6],6],
        [[3,9,3],2],
        [[9,3],2],
        [[9,4],2],
        [[1,2,3,4,5],0],
        [[1],0]
    ]
    for case in cases:
        print(minimumReplacement(case[0]),'|',case[1])
