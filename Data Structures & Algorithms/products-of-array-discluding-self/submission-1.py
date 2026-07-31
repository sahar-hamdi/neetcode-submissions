class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)

        if zeros > 1:
            return [0] * len(nums)

        
        res = 1

        for i in nums:
            if i != 0:
                res *= i

        ans = []

        for i in range(len(nums)):
            if zeros == 1:
                if nums[i] == 0:
                    ans.append(res)

                else:
                    ans.append(0)

            else:
                ans.append(res // nums[i])

        return ans 