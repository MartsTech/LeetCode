# O(n) space
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    # O(log(n)) time
    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    # O(log(n)) time
    def union(self, i: int, j: int) -> bool:
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return False
        if self.rank[pi] < self.rank[pj]:
            self.parent[pi] = pj
        elif self.rank[pi] > self.rank[pj]:
            self.parent[pj] = pi
        else:
            self.parent[pj] = pi
            self.rank[pi] += 1
        return True

class Solution:
    # O(n*log(n)) time | O(n) space
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        uf = UnionFind(n)
        for i, j in connections:
            uf.union(i, j)
        components = set(uf.find(i) for i in range(n))
        if len(components) == 1:
            return 0
        return len(components) - 1