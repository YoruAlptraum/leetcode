def isStrictlyPalindromic(n: int) -> bool:
    for b in range(2,n-1):
        if not palindromicBase(n,b):
            return False
        
def palindromicBase(num, base) -> str:
    if num == 0:
        return 0
    res = ""
    while num > 0:
        res = str(num%base) + res
        num //= base
    return res == reversed(res)

# the most optimal resolution for this problem is return False since the only possible answers for base of n-2 is not palindromic
# although, ironically, this code ran in a smaller time than when I tried the return False code on leetcode
    
if __name__ == "__main__":
    cases = [
        [9],
        [4]
    ]
    # only answer for this problem is False
    for case in cases:
        print(isStrictlyPalindromic(case[0]))
    # for i in range(100):
    #     print(i, palindromicBase(i,3), end="\n==============\n")
