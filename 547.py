class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if end not in visited and isConnected[start][end] == 1:
                    dfs(end)
        
        visited = set()
        province = 0

        for start in range(len(isConnected)):
            if start not in visited:
                province += 1
                dfs(start)
        return province