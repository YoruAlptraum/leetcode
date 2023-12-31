# simple approach, just create arrays for each and append or pop if it's a char or a backspace
# time O(n) space O(n)
def backspaceCompare(s: str, t: str) -> bool:
    s1,s2 = [],[]
    for c in s:
        if c != '#':
            s1.append(c)
        elif s1:
            s1.pop()
    for c in t:
        if c != '#':
            s2.append(c)
        elif s2:
            s2.pop()
    return s1 == s2

# two pointers approach for O(1) space
def backspaceCompare2(s: str, t: str) -> bool:
    ls, lt = len(s)-1, len(t)-1

    def updateCount(list: str, n: int) -> int:
        counter = 0
        while n >= 0:
            if list[n] == '#':
                counter += 1
                n -= 1
            elif counter > 0:
                counter -= 1
                n -= 1
            else:
                break
        return n

    while ls >=0 or lt>=0:
        ls = updateCount(s,ls)
        lt = updateCount(t,lt)

        # if both are negative it means they are both empty
        if lt < 0 and ls < 0:
            break
        # if different means false since there you can no longuer remove the char
        elif t[lt] != s[ls]:
            return False
        # if one has ended and the other has not
        elif (lt < 0 or ls < 0) and (lt >= 0 or ls >= 0):
            return False
        ls -= 1
        lt -= 1
    return True

if __name__ == "__main__":
    cases = [
        ["ab##", "c#d#", True],
        ["a#c", "b", False],
        ["ab#c", "ad#c", True],
        ["xywrrmp","xywrrmu#p",True],
        ["xywrrmp","xywrrm#p",False],
        ["mp","m#p",False],
        ["y#fo##f","y#fx#o##f",True],
        ["y#fo##f","y#f#o##f",True],
        ["a##c","#a#c",True],
        ["bbbextm","bbb#extm",False],
        ["aaa###a","aaaa###a",False]
    ]
    
    for c in cases:
        print('pass' if backspaceCompare2(c[0],c[1]) == backspaceCompare(c[0],c[1]) else 'fail')


