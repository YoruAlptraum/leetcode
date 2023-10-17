from typing import List

def minOperations(boxes: str) -> List[int]:
    n = len(boxes)
    arr = [0] * n
    lcost, rcost = int(boxes[0]), int(boxes[-1])
    # check left to right
    for i in range(1,n):
        arr[i] += lcost + arr[i-1]
        lcost += int(boxes[i])
    prev = 0
    # check right to left
    for i in range(n-2,-1,-1):
        prev += rcost
        arr[i] += prev
        rcost += int(boxes[i])
    return arr

if __name__ == "__main__":
    cases = [
        ["110", [1,1,3]],
        ["001011", [11,8,5,4,3,4]],
        ['1000000',[0,1,2,3,4,5,6]]
    ]

    for case in cases:
        print(minOperations(case[0]),'|',case[1])
