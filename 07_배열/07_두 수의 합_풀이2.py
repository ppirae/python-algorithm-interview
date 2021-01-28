# 풀이2 in을 이용한 탐색
# 864 밀리초

def twoSum(slef, num: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1]:
            return nums.index(n), nums[i+1:].index(complement) + (i+1)
