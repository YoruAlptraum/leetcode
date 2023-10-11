def balancedStringSplit(s: str) -> int:
    b = 0
    res = 0
    for i in s:
        if i == "R":
            b += 1
        else:
            b -= 1
        if b == 0:
           res += 1
    return res 

if __name__ == "__main__":
    cases = [
        ["RLRRLLRLRL",4],
        ["RLRRRLLRLL",2],
        ["LLLLRRRR",1]
    ]
    for case in cases:
        print(balancedStringSplit(case[0]),'|',case[1])