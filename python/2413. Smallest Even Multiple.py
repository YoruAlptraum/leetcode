def smallestEvenMultiple(n: int) -> int:
    while n % 2 !=0:
        n += n
    return n

# it can also be written as 
def smallestEvenMultiple2(n: int) -> int:
    return n if n % 2 == 0 else n * 2
    # can also be written as 
    # return n * (n % 2 + 1)

if __name__ == "__main__":
    cases = [
        [5,10],
        [6,6],
        [149,298],
        [150,150]
    ]

    for case in cases:
        print(smallestEvenMultiple2(case[0]),'|',case[1])