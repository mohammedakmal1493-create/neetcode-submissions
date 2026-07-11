class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()

        for i in range(len(nums)):
            seen={}
            for j in range(i+1,len(nums)):
                third= -(nums[i] + nums[j])
                if third in seen:
                    triplet = tuple(sorted([nums[i],nums[j],third]))
                    res.add(triplet)
                seen[nums[j]]=j
                
        ans = [list(x) for x in res]
        return ans