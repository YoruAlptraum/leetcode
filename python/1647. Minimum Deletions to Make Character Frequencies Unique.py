from collections import Counter

def minDeletions(s: str) -> int:
    chars = Counter(s)
    d = 0
    lis = []
    for i in chars.values():
        while i in lis and i != 0:
            i -= 1
            d += 1
        lis.append(i)
    return d

if __name__ == "__main__":
    print(minDeletions(s = "aab")) # Output: 0
    print(minDeletions(s = "aaabbbcc")) # Output: 2
    print(minDeletions(s = "ceabaacb")) # Output: 2
