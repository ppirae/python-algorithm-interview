# 풀이2 파이썬다운 방식
# 104 밀리초

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    return list(zip(*collections.Counter(nums).most_common(k)))[0]
