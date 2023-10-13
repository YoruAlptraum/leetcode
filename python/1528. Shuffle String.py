from typing import List

# naive approach, just rearange in a new array and return the array as a string
def restoreString(s: str, indices: List[int]) -> str:
    res = [0] * len(s)
    for c,i in zip(s,indices):
        res[i] = c
    return ''.join(res)

# adding to string instead of using a new array
# after testing it ended up actually being slightly slower and consuming slightly more memory
# it's still within margin of error so the difference seems to be negligible
def restoreString2(s: str, indices: List[int]) -> str:
    res = ''
    for i in range(len(s)):
        res += s[indices.index(i)]
    return res

if __name__ == "__main__":
    cases = [
        ["codeleet",[4,5,6,7,0,1,2,3],"leetcode"],
        ["codeleet",[4,0,2,1,5,6,7,3],"oedtclee"],
        ["abc",[0,1,2],"abc"]
    ]
    for case in cases:
        print(restoreString(case[0],case[1]),'|',case[2])
