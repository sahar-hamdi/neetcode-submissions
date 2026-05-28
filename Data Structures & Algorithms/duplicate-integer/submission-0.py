class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = 0
        sorted_nums = sorted(nums)
        n = len(nums)
        for i in range(n-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                cnt += 1

        if cnt >= 1:
            return True 
        else:
            return False