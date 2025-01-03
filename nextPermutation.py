# Time:O(n) 3 pass 
# Space:O(1)
# Leetcode: yes
# Issues:No 

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2                                                 

        while i>=0 and nums[i] > nums[i+1]:                     # find the breach at index i  
            i-=1
        # i is the breach

        if i >=0:
            j = n-1
            while nums[j] <= nums[i]:
                j-=1
        # j is the next bigger element after i so swap
        
            nums[i],nums[j] = nums[j], nums[i]                  # swap i and j th elements

        nums[i+1:] = nums[i+1:][::-1]                           # reverse the string after i