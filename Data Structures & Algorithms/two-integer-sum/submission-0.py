class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}

        for idx, num in enumerate(nums):
            difference = target - num
            if difference in diff_map:
                return [diff_map[difference], idx]
            
            diff_map[num] = idx
