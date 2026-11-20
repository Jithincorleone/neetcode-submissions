class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_num=list(set(nums))
        sorted_num=sorted(sorted_num)
        L, length=0,0
        
        for R in range(len(sorted_num)):
            if sorted_num[R] - sorted_num[R-1] >1:
                L=R
            
            length=max(length, R-L+1)
        return length