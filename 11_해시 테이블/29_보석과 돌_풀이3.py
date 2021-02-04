# 풀이3 Counter로 계산 생략
# 32 밀리초, 코드 7줄

def numJewelsInStones(self, J: str, S: str) -> int:
    freqs = collections.Counter(S) # 돌(S) 빈도 수 계산
    count = 0

    # 비교 없이 보석(J) 빈도 수 합산
    for char in J:
        count += freqs[char]

    return count
