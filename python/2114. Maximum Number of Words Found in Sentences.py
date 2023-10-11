from typing import List

def mostWordsFound(sentences: List[str]) -> int:
    ans = 0
    for s in sentences:
        arr = s.split(' ')
        count = 0
        for i in arr:
            if len(i) > 0:
                count += 1
        if count > ans:
            ans = count
    return ans

def mostWordsFound(sentences: List[str]) -> int:
    ans = 0
    for s in sentences:
        ans = max(s.count(" "), ans)
    return ans + 1

if __name__ == "__main__":
    cases = [
        [["alice and bob love leetcode", "i think so too", "this is great thanks very much"],6],
        [["please wait", "continue to fight", "continue to win"],3]
    ]
    for c in cases:
        print(mostWordsFound(c[0]),'|',c[1])