from typing import List

def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    snums = sorted(nums)
    map = {}
    for i, n in enumerate(snums):
        if n not in map:
            map[n] = i
    return [map[i] for i in nums]

if __name__ == "__main__":
    cases = [
        [[8,1,2,2,3],[4,0,1,1,3]],
        [[6,5,4,8], [2,1,0,3]],
        [[7,7,7,7],[0,0,0,0]]
    ]

    for case in cases:
        print(smallerNumbersThanCurrent(case[0]) == case[1])
