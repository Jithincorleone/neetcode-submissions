class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        window=[]
        l=0
        window_cnt=0
        window_avg=0
        
        for r in range(len(arr)):
            window_size=r-l+1
            
            if window_size > k:
                window.remove(arr[l])
                l+=1            
            window.append(arr[r])
            
            if len(window)==k:
                window_avg=sum(window)/k
            
            if window_avg >= threshold:
                window_cnt+=1
        return window_cnt
