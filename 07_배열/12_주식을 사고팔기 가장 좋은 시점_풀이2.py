# 풀이2 저점과 현재 값과의 차이 계산
# 64 밀리초

def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxprice

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit
