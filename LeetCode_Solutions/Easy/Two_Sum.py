
"""
Problem: Two Sum
Platform: LeetCode
Difficultiy: Easy

Time complexity: O(N)
space COmplexity: O(N)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        set_nums = set(nums)
        lis=[]
        for i, j in enumerate(nums):
            
            if(target-j in set_nums):
                
                try:
                    idx = nums.index(target - j)
                    if idx != i:
                        return [i,nums.index(target-j)]
                except:
                    continue

        return []
        
        