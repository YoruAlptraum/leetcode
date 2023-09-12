from typing import List

def generate(numRows: int) -> List[List[int]]:
    ans = []
    for i in range(numRows):
        arr = [1] * (i + 1)
        if i > 1:
            for j in range(1,len(arr)-1):
                arr[j] = ans[i-1][j-1] + ans[i-1][j]
        ans.append(arr)
    return ans

if __name__ == "__main__":
    print(generate(5))
