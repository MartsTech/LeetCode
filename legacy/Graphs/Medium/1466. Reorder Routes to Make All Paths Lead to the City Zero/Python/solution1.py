class Solution:
    # O(n) time | O(n) space
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v in connections:
            graph[u][v] = 1
            graph[v][u] = 0
        return self.dfs(0, -1, graph)[1]

    def dfs(self, node: int, parent: int, graph: Dict[int, Dict[int, int]]) -> Tuple[int, int]:
        total = 0
        reversed = 0
        for child, direction in graph[node].items():
            if child != parent:
                traversed, rev = self.dfs(child, node, graph)
                total += traversed
                reversed += rev
                if graph[node][child] != 0:
                    reversed += 1
                total += 1
        return total, reversed