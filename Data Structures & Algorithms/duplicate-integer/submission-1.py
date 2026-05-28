class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}

        for num in nums:
            if num in dict_:
                dict_[num] += 1
            else:
                dict_[num] = 1

        for key, val in dict_.items():
            if val > 1 :
                return True
        return False