import timeit
from functools import partial

# using if i == 9 | 0.011936699971556664
# using string in | 0.001253599999472499
def minPartitions(n: str) -> int:
    m = 0
    if '9' in n:
        return '9'
    for i in n:
        I = int(i)
        if I > m:
            m = I
    return m

# 0.0065234999638050795
def minPartitions2(n: str) -> int:
    m = ord('0')
    if '9' in n:
        return '9'
    for i in n:
        I = ord(i)
        if I > m:
            m = I
    return int(chr(m))

# 0.00202519993763417
def minPartitions3(n: str) -> int:
    for i in range(9,-1,-1):
        if str(i) in n: 
            return i

if __name__ == "__main__":
    cases = [
        ["32",3],
        ["82734",8],
        ["27346209830709182346",9]
    ]
    for c in cases:
        print(minPartitions3(c[0]),'|',c[1])
    part = partial(minPartitions3,cases[2][0])
    print(timeit.timeit(part, number=10000))
