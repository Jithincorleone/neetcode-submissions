from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ctr=Counter(nums)

        mst_common=ctr.most_common()

        sorted_list=sorted(mst_common, key=lambda k:k[1], reverse=True)
        sorted_list=[row[0] for row in sorted_list]

        return sorted_list[:k]

