 
def isHappy(n: int) -> bool:
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        sum = n
        n = 0
        while sum > 0:
            n += (sum % 10) ** 2
            sum = sum//10
    return True

if __name__ == "__main__":
    for i in range(420):
        print(isHappy(i))
