class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        def dfs_b(node, parent, xor_all_subtree, xor_a):
            nonlocal ans
            curr_xor = nums[node]
            for nei in graph[node]:
                if nei != parent:
                    xor_b = dfs_b(nei, node, xor_all_subtree, xor_a)
                    curr_xor ^= xor_b
                    xor_c = xor_all_subtree ^ xor_b
                    ans = min(ans, max(xor_a, xor_b, xor_c) - min(xor_a, xor_b, xor_c))
            return curr_xor


        def dfs_a(node, parent, xor_all_tree):
            curr_xor = nums[node]
            for nei in graph[node]:
                if nei != parent:
                    xor_a = dfs_a(nei, node, xor_all_tree)
                    curr_xor ^= xor_a
                    dfs_b(node, nei, xor_all_tree ^ xor_a, xor_a)
            return curr_xor

        ans = inf
        dfs_a(0, -1, reduce(xor, nums))
        return ans