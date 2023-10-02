from typing import List

def isMonotonic(nums: List[int]) -> bool:
    asc = True
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            asc = False
            break
    if not asc:
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                return False
    return True

def isMonotonic2(nums: List[int]) -> bool:
    d = 0
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            if d == -1:
                return False
            else:
                d = 1
        elif nums[i] < nums[i-1]:
            if d == 1:
                return False
            else:
                d = -1
    return True

if __name__ == "__main__":
    testcases = [
        [[1,2,2,3], True],
        [[6,5,4,4], True],
        [[1,3,2], False],
        [[2,3,1], False],
    ]
    for t in testcases:
        print(isMonotonic(t[0]),'|',t[1])
        print(isMonotonic2(t[0]),'|',t[1])
