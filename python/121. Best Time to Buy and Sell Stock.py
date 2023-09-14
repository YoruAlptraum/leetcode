from typing import List

def maxProfit(prices: List[int]) -> int:
    profit = 0
    buy = prices[0]
    for i in prices:
        if i - buy > profit:
            profit = i - buy
        if i < buy:
            buy = i
    return profit

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4])) # 5
    print(maxProfit([7,6,4,3,1])) # 0
