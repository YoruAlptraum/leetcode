from typing import List

def pivotArray(nums: List[int], pivot: int) -> List[int]:
    left, right, p = [], [], []
    for n in nums:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
        else:
            p.append(n)
    return left + p + right

if __name__ == "__main__":
    cases = [
        [[9,12,5,10,14,3,10], 10, [9,5,3,10,10,12,14]],
        [[-3,4,3,2], 2, [-3,2,4,3]]
    ]
    for case in cases:
        print('passed' if pivotArray(case[0],case[1])==case[2] else 'failed')