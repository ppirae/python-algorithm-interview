# 풀이2 데크 자료형을 이용한 최적화
# 64 밀리초

def isPalindrome(self, s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = colections.deque

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
