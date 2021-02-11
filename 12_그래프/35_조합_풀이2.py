# 풀이2 itertools 모듈 사용
# 76 밀리초

def combine(self, n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n+1), k))
