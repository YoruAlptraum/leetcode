from typing import List

# with dictionary
def finalValueAfterOperations(operations: List[str]) -> int:
    op = {"++X":1, "X++":1, "--X":-1,"X--":-1}
    x = 0
    for i in operations:
        x += op[i]
    return x

# with for loop
def finalValueAfterOperations2(operations: List[str]) -> int:
    x = 0
    for i in operations:
        if i == 'X++' or i == '++X':
            x += 1
        else:
            x -= 1
    return x

if __name__ == '__main__':
    cases = [
        [["--X","X++","X++"],1],
        [["++X","++X","X++"],3]
    ]
    for i in cases:
        print(finalValueAfterOperations2(i[0]),'|',i[1])
