# 풀이2 defaultdict를 이용한 비교 생략
# 28 밀리초, 코드 10줄

def numJewelsInStones(self, J: str, S: str) -> int:
    freqs = collections.defaultdict(int)
    count = 0

    # 비교 없이 돌(S) 빈도 수 계산
    for char in S:
        freqs[char] += 1

    # 비교 없이 보석(J) 빈도 수 합산
    for char in J:
        count += freqs[char]

    return count
