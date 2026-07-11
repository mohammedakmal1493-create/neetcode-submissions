class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new=[]

        for i in range(len(nums)):
            multi=1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    multi*=nums[j]
            new.append(multi)

        return new
