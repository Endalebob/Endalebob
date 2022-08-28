class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(set)
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        deq = []
        for i in graph:
            if len(graph[i]) == 1:
                deq.append(i)
        while n>2:
            curr = deq
            n -=len(curr)
            new_l = []
            for i in curr:
                for j in graph[i]:
                    graph[j].remove(i)
                    if len(graph[j]) == 1:
                        new_l.append(j)
            deq = new_l
        return deq