from typing import List

def getRow(rowIndex: int) -> List[int]:
    ans = [1] * (rowIndex+1)
    prev = ans.copy()
    for i in range(1,rowIndex):
        for j in range(1,i+1):
            ans[j] = prev[j] + prev[j-1]
        prev = ans.copy()
    return ans

if __name__ == "__main__":
    print(getRow(0))
    print(getRow(1))
    print(getRow(2))
    print(getRow(6))
