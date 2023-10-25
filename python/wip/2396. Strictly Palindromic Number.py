def isStrictlyPalindromic(n: int) -> bool:
    for b in range(2,n-1):
        
    return True

if __name__ == "__main__":
    cases = [
        [9],
        [4]
    ]
    # only answer for this problem is False
    for case in cases:
        print(isStrictlyPalindromic(case[0]))
