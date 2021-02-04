# 풀이4 파이썬다운 방식
# 28 밀리초, 코드 1줄

def numJewelsInStones(self, J: str, S: str) -> int:
    return sum(s in J for s in S)
