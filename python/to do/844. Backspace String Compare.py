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
    bs, bt = 0, 0
    while ls >0 or lt>0:
        while ls > 0:
            if s[ls] == '#':
                bs += 1
                ls -= 1
            elif bs > 0:
                bs -= 1
                ls -= 1
            else:
                break
        while lt > 0:
            if t[lt] == '#':
                bt += 1
                lt -= 1
            elif bt > 0:
                bt -= 1
                lt -= 1
            else:
                break
        if t[lt] != s[ls]:
            return False
        # if they are the same but one of them has ended return false 
        elif t[lt] == s[ls] and (lt == 0 or ls == 0):
            return False
        if ls > 0:
            ls -= 1
        if lt > 0:
            ls -= 1
    return True

if __name__ == "__main__":
    cases = [
        ["ab##", "c#d#", True],
        ["ab#c", "ad#c", True],
        ["a#c", "b", False],
        ["xywrrmp","xywrrmu#p",True],
        ["xywrrmp","xywrrm#p",False],
        ["mp","m#p",False],
        ["y#fo##f","y#fx#o##f",True],
        ["y#fo##f","y#f#o##f",True],
        ["a##c","#a#c",True]
    ]
    
    for c in cases:
        print('pass' if backspaceCompare2(c[0],c[1]) == c[2] else 'fail')


