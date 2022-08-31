class Solution:
    def findOrder(self, c: int, pre: List[List[int]]) -> List[int]:
        indegree = [0]*c
        ans = []
        gl_vstd = set()
        graph = defaultdict(list)
        for i,j in pre:
            graph[j].append(i)
            indegree[i]+=1
        root = []
        for i in range(c):
            if indegree[i] == 0:
                root.append(i)
        def dfs(idx):
            if idx in gl_vstd:
                return True
            if idx in vstd:
                return False
            vstd.add(idx)
            for i in graph[idx]:
                if not dfs(i):
                    return False
            vstd.remove(idx)
            gl_vstd.add(idx)
            ans.append(idx)
            return True
        for i in root:
            vstd = set()
            if not dfs(i):
                return []
        if len(ans) == c:
            return ans[::-1]
        return []
            