class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)

        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                res = nums[i] + nums[l] + nums[r]

                if res == 0:
                    answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif res < 0:
                    l += 1
                else:
                    r -= 1

        return answer
