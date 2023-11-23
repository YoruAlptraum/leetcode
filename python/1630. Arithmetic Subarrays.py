from typing import List

# this was the first algorithm that came to mind when seeing the constraints and examples of the problem
# after seeing the best answers i think i did pretty well, the only difference for the top answers was that they had more edge cases included but the code was mostly the same

def checkArithmeticSubarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    ans = []
    for a,b in zip(l,r):
        ans.append(checkArithmetic(sorted(nums[a:b+1])))
    return ans

def checkArithmetic(sub: List[int]) -> bool:
    if len(sub) <= 1:
        return False
    dif = sub[1] - sub[0]
    for i in range(1,len(sub)):
        if sub[i] - sub[i-1] != dif:
            return False
    return True

if __name__ == "__main__":
    cases = [
        [[4,6,5,9,3,7], [0,0,2], [2,3,5]],
        [[-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10],[0,1,6,4,8,7], [4,4,9,7,9,10]]
    ]

    for c in cases:
        print(checkArithmeticSubarrays(*c))
