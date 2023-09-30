
def reverseVowels(s: str) -> str:
    l = 0
    r = len(s) -1
    if r == 0:
        return s
    v = set('AEIOUaeiou')
    charlist = [' '] * len(s)
    while l <= r:
        if s[l] not in v:
            charlist[l] = s[l]
            l+=1
        if s[r] not in v:
            charlist[r] = s[r]
            r-=1
        if s[l] in v and s[r] in v:
            charlist[r] = s[l]
            charlist[l] = s[r]
            l+=1
            r-=1
    return ''.join(charlist)

if __name__ == '__main__':
    test = [
        ["hello", "holle"],
        ["leetcode","leotcede"],
        [".","."],
        ["aA","Aa"],
        ["abA","Aba"]
    ]
    for t in test:
        res = reverseVowels(t[0])
        print('passed' if res == t[1] else 'failed','|', res,'|',t[1])
