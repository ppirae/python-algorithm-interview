# 풀이1 오름차순 풀이
# 332 밀리초

def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair =[]

    return sum
