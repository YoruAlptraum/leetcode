from typing import List

def candy(ratings: List[int]) -> int:
    n = len(ratings)
    candies = [1] * n
    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] +1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] +1)
                
    print(candies)
    return sum(candies)

if __name__ == "__main__":
    print(candy(ratings = [1,2,2]),"| 4") # 4
                        # [0,1,0]
    print(candy(ratings = [1,0,2]),"| 5") # 5
                        # [1,0,1]
    print(candy(ratings = [1,3,2,2,1]),"| 7") # 7
                        # [0,1,0,1,0]
    print(candy(ratings = [1,3,4,5,2]),"| 11") # 11
                        # [1,2,3,4,1]
    print(candy(ratings = [29,51,87,87,72,12]),"| 12") # 12
                        # [ 1, 2, 3, 3, 2, 1]
    print(candy(ratings = [1,2,3,4,5,6,7]),"| 28") # 28
                        # [0,1,2,3,4,5,6]
    print(candy(ratings = [7,6,5,4,3,2,1]),"| 28") # 28
                        # [6,5,4,3,2,1,0]
