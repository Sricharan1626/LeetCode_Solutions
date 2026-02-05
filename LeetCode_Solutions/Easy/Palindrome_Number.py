"""
Problem: Palindrome Number
Platform: LeetCode
Difficultiy: Easy

Time complexity: O(N)
space COmplexity: O(N)
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x_palindrome = str(x)
        if(x_palindrome[::-1] == x_palindrome):
            return True
        return False
        