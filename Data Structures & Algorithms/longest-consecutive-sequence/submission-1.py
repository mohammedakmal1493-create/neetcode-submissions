class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, currposition = 0, num  #streak is the streak like 2,3,4,5 if anything comes after 5 like 10 , the streak brakes and new streak starts
            while currposition in store:
                streak += 1
                currposition += 1
            res = max(res,streak)
        return res