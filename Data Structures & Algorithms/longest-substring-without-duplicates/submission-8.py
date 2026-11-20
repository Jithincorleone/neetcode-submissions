class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L, length=0,0
        windows=set()
        
        for R in range(len(s)):
            while s[R] in windows:
                windows.remove(s[L])
                L+=1
            windows.add(s[R])                
            length=max(length, R-L+1)
        return length


        