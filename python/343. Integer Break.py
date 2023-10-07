def integerBreak(n):
    if n < 4:
        return n-1
    
    ans = 1
    while n > 4:
        ans *= 3
        n -= 3
    return ans * n


if __name__ == '__main__':
    for i in range(2,58):
        print(i,integerBreak(i))
