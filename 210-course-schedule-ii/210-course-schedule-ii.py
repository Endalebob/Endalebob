class Solution:
    def findOrder(self, c: int, pre: List[List[int]]) -> List[int]:
        indegree = [0]*c
        graph = defaultdict(list)
        for i,j in pre:
            graph[j].append(i)
            indegree[i]+=1
        deq = deque()
        for i in range(c):
            if indegree[i] == 0:
                deq.append(i)
        ans = []
        print(indegree)
        while deq:
            for i in range(len(deq)):
                j = deq.popleft()
                ans.append(j)
                for k in graph[j]:
                    indegree[k] -= 1
                    if indegree[k] == 0:
                        deq.append(k)
        if len(ans) == c:
            return ans
        return []