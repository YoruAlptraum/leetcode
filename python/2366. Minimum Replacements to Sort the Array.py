from typing import List

# initial approach updating the previous num
def minimumReplacement(nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)-2,-1,-1):
        # if cur is greater than prev
        if nums[i] > nums[i+1]:
            # number of times the number should be divided by
            t = nums[i] // nums[i+1] 
            # if mod it means the division is not perfect
            # if the division is not perfect the previous needs to be updated to the result of the division
            if nums[i] % nums[i+1]:
                nums[i] = nums[i] // (t+1) 
                res += t
            # if mod is 0 and the division is perfect, the cur will be updated to be equal the prev 
            else:
                nums[i] = nums[i+1]
                res += t - 1
    return res

# using prev variable instead
# increases speed by quite a bit with the cost of a bit of memory
def minimumReplacement2(nums: List[int]) -> int:
    prev = nums[-1]
    res = 0
    for i in range(len(nums) -2, -1,-1):
        if nums[i] > prev:
            t = nums[i]//prev
            if nums[i] % prev:
                res+=t 
                prev = nums[i] // (t+1)
            else:
                res += t-1
        else:
            prev = nums[i]
    return res

if __name__ == "__main__":
    cases = [
        [[1,13,15,2,5,14,12,17],20],
        [[12,9,7,6],6],
        [[3,9,3],2],
        [[1,2,3,4,5],0],
        [[368,112,2,282,349,127,36,98,371,79,309,221,175,262,224,215,230,250,84,269,384,328,118,97,17,105,342,344,242,160,394,17,120,335,76,101,260,244,378,375,164,190,320,376,197,398,353,138,362,38,54,172,3,300,264,165,251,24,312,355,237,314,397,101,117,268,36,165,373,269,351,67,263,332,296,13,118,294,159,137,82,288,250,131,354,261,192,111,16,139,261,295,112,121,234,335,256,303,328,242,260,346,22,277,179,223],17748]
    ]
    scases = [
        [[9,1],8],
        [[15,2],7],
        [[9,3],2],
        [[9,4],2],
        [[9,3],2],
        [[1],0],
        [[16,5],3]
    ]
    for case in cases:
        print(minimumReplacement(case[0]),'|',case[1],end='\n=====================================\n')
    # print(minimumReplacement(cases[1][0]))