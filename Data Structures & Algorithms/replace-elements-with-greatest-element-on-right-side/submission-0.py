class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(0, len(arr)):
            current_val=arr[i]
            if i==len(arr)-1:
                offset=len(arr)-1
            else:
                offset=i+1
            max_val=max(arr[offset:])
            #if current_val < max_val:
            arr[i]=max_val
        
        arr[len(arr)-1]=-1

        return arr
