class Solution:
    def maxFreeTime(self, t: int, st: List[int], et: List[int]) -> int:

        st.append(t)
        et.append(t)
        
        sic = [(st[0] - 0, 0), (-1, -1), (-1, -1)]
        # print(sic)

        for i in range(1, len(st)):
            gap = (st[i] - et[i-1], i)
            # print(gap)
            if gap[0] > sic[2][0]:
                sic[2] = gap 
                sic.sort(reverse=True, key=lambda x: x[0])
            # print(sic)
        print(sic)
        mgap = 0
        for i in range(len(st) - 1):
            if i == 0:
                left = 0
            else:
                left = et[i - 1]
            egap = et[i] - st[i]
            adjgap = st[i+1] - left
            print(adjgap)
            for j in sic:
                if j[0] >= egap and j[1] != i  and j[1] != i+1:
                    mgap = max(mgap, adjgap)
                else:
                    mgap = max(mgap, (adjgap - egap))
        return mgap
            
        