def isSubsequence(s: str, t: str) -> bool:
    tl = len(t)
    sl = len(s)

    if sl == 0: return True
    if tl == 0: return False
    p = 0

    for i in range(tl):
        if s[p] == t[i]:
            p += 1
        if p > sl-1:
            return True
    return False

if __name__ == "__main__":
    testcases = [
        ["abc","ahbgdc",True], 
        ["axc","ahbgdc",False],
        ["b","abc",True],
        ["abba","ahbdc",False],
        ["abbc","ahbdc",False],
        ["b","c",False],
        ["axc","",False],
    ]
    for i in testcases:
        print("passed" if isSubsequence(i[0],i[1]) == i[2] else "failed")