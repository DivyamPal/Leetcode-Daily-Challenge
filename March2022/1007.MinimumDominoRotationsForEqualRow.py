from collections import Counter
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        dic1=Counter(tops)
        dic2=Counter(bottoms)
        n1,n2=len(tops),len(bottoms)
        swap=0
        for i in range(1,7):
            if dic1[i]+dic2[i]>=n1:
                swap=i
                break
        print(swap)
        if not swap:
            return -1
        for i in range(n1):
            if swap not in [tops[i],bottoms[i]]:
                return -1
        return min(n1-dic1[swap],n2-dic2[swap])
        
