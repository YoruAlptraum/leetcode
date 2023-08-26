from typing import List

def isAcronym(words: List[str], s: str) -> bool:
    wlen = len(words)
    if wlen != len(s):
        return False
    for i in range(wlen):
        if words[i][0] != s[i]:
            return False
    return True

print(isAcronym(words = ["alice","bob","charlie"], s = "abc"))
print(isAcronym(words = ["an","apple"], s = "a"))
print(isAcronym(words = ["an","apple"], s = "aa"))
print(isAcronym(words = ["an"], s = "aa"))
