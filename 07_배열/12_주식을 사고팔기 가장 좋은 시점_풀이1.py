# 풀이1 브루트 포스로 계산
# 타임 아웃

def maxProfit(self, prices: List[int]) -> int:
    max_price = 0

    for i, n in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price
