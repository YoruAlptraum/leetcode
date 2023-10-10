import timeit
from functools import partial

# using string.replace
def interpret(command: str) -> str:
    return command.replace('()','o').replace('(al)','al')

# using for loop
def interpret2(command: str) -> str:
    ans = ''
    prev = ''
    for i in command:
        if i == 'G':
            ans += i
        elif i == ')':
            if prev == '(':
                ans += 'o'
            else:
                ans += 'al'
        prev = i
    return ans

if __name__ == '__main__':
    cases = [
        ["G()(al)","Goal"],
        ["G()()()()(al)","Gooooal"],
        ["(al)G(al)()()G","alGalooG"]
    ]
    for case in cases:
        part = partial(interpret2,case[0])
        print(interpret2(case[0]),'|',case[1])
        print(timeit.timeit(part, number=10000))
