# 풀이2 itertools 모듈 사용
# 36 밀리초

def permute(self, nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))
