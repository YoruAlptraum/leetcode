from typing import List

def countBits(n: int) -> List[int]:
    ans = []
    for i in range(n + 1):
        sum = 0
        s = str(bin(i))
        print(s)
        for j in range(2,len(s)):
            sum += int(s[j])
        ans.append(sum)
    return ans

if __name__ == "__main__":
    print(countBits(10))
    print([0,1,1,2,1,2,2,3,1,2,2])