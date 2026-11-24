class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n=len(nums)

        prefix_sum=[0]*(n+1)

        for i in range(n):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]
        
        for i in range(n):
            prefix_left=prefix_sum[i]
            prefix_right=prefix_sum[n]-prefix_sum[i+1]

            if prefix_left == prefix_right:
                return i
        
        return -1


        

