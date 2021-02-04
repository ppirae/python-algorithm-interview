# 풀이1 해시 테이블을 이용한 풀이
# 32 밀리초, 코드 14줄

def numJewelsInStones(self, J: str, S: str) -> int:
    freqs = {}
    count = 0

    # 돌(S)의 빈도 계산
    for char in s:
        if char not in freqs:
            freqs[char] = 1
        else:
            freq[char] += 1

    # 보석(J)의 빈도 수 합산
    for char in s:
        if char in freqs:
            count += freq[char]

    return count
