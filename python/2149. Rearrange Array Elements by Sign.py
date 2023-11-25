from typing import List

def base(nums: List[int]) -> List[int]:
    n,p = [],[]
    for i in nums:
        if i > 0:
            n.append(i)
        else:
            p.append(i)
    for i in range(len(nums)):
        if i % 2 == 0:
            nums[i] = n.pop(0)
        else:
            nums[i] = p.pop(0)
    return nums

def rearrangeArray(nums: List[int]) -> List[int]:
    n,p = 1,0
    a = [0]*len(nums)
    for i in nums:
        if i > 0:
            a[p] = i
            p += 2
        else:
            a[n] = i
            n += 2
    return a

if __name__ == "__main__":
    cases = [
        [3,1,-2,-5,2,-4],
        [-1,1],
        [3,1,2,-4,-2,-5]
    ]

    for c in cases:
        print('pass' if base(c) == rearrangeArray(c) else 'failed')
