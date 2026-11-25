class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum={0:1}
        res=0
        prefix_j=0

        for num in nums:
            
            prefix_j+=num

            prefix_i=prefix_j - k

            res+=prefix_sum.get(prefix_i,0)

            prefix_sum[prefix_j] = 1 + prefix_sum.get(prefix_j, 0)
        
        return res





        