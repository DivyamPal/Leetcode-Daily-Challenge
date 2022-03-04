class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(query_glass+2)] for x in range(query_row + 2)]
        dp[0][0]=poured
        for i in range(query_row):
            for j in range(0,query_glass+1):
                remaining=max(dp[i][j]-1,0)
                dp[i+1][j]+=remaining/2.0
                dp[i+1][j+1]+=remaining/2.0
        return min(dp[query_row][query_glass],1.0)
        
