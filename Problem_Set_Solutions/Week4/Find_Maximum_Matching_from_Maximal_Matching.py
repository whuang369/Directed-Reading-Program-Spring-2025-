from collections import deque

class MaximumMatching:
    def __init__(self, n):
        """Initialize"""
        self.n = n
        self.adj = [[] for i in range(n)]
        self.match = [-1] * n
        self.parent = [-1] * n

    def add_edge(self, u, v):
        """Adds an edge between u and v"""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs_augmenting_path(self):
        """Finds an augmenting path using BFS and augments the matching"""
        queue = deque()
        self.parent = [-1] * self.n
        free_nodes = set()

        for i in range(self.n):
            if self.match[i] == -1:
                queue.append(i)
                free_nodes.add(i)

        while queue:
            u = queue.popleft()

            for v in self.adj[u]:
                if self.match[v] == -1 and v not in free_nodes:
                    self.augment_path(u, v)
                    return True

                elif self.match[v] != -1 and self.parent[self.match[v]] == -1:
                    self.parent[self.match[v]] = v
                    self.parent[v] = u
                    queue.append(self.match[v])

        return False

    def augment_path(self, u, v):
        """Flips the edges along the found augmenting path to increase matching size"""
        while True:
            prev_match = self.match[u]
            self.match[u] = v
            self.match[v] = u

            if prev_match == -1:
                break

            u = self.parent[prev_match]
            v = prev_match

    def find_maximum_matching(self, initial_matching):
        """Finds the maximum matching starting from a given maximal matching"""
        for u, v in initial_matching:
            self.match[u] = v
            self.match[v] = u

        while self.bfs_augmenting_path():
            pass

        max_matching = set()
        for u in range(self.n):
            if self.match[u] != -1 and u < self.match[u]:
                max_matching.add((u, self.match[u]))

        return max_matching