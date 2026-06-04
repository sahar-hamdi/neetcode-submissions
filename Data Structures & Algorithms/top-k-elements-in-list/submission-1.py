class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        result = []

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        sorted_dict = sorted(freq_dict.items(), key = lambda x: x[1], reverse = True)

    

        for i in range(k):
            result.append(sorted_dict[i][0])


        return result