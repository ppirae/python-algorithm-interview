# 풀이3 파이썬다운 방식
# 284 밀리초

def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
