class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        result = []
        
        nums.sort()
        
        for i in range(n-3):
            for j in range(i+1, n-2):
                t = target - (nums[i] + nums[j])
                left = j + 1
                right = n - 1
                while left < right:
                    if nums[left] + nums[right] < t:
                        left += 1
                    elif nums[left] + nums[right] > t:
                        right -= 1
                    else:
                        result.append((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        
        return set(result)