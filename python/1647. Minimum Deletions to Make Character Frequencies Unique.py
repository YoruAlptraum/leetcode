
def minDeletions(s: str) -> int:
    d = 0
    freq = {}
    # count freq of each char
    i = 0
    for i in s:
        if i in freq:
            freq[i] += 1            
        else:
            freq[i] = 1
    lis = []
    for i in freq.values():
        while i in lis and i != 0:
            i -= 1
            d += 1
        if i not in lis:
            lis.append(i)
    return d

if __name__ == "__main__":
    print(minDeletions(s = "aab")) # Output: 0
    print(minDeletions(s = "aaabbbcc")) # Output: 2
    print(minDeletions(s = "ceabaacb")) # Output: 2
