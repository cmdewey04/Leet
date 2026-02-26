# Last updated: 2/26/2026, 1:36:34 PM
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hSet = {i:[] for i in range(n)}
        for e1,e2 in edges:
            hSet[e1].append(e2)
            hSet[e2].append(e1)
        
        
        visiting = set()
        seen = set()
        connected = False
        def dfs(node, parentN):

            #if edge is not the one that we just came from
            #go down there
            #if node already in visited 

            #we found a cycle on our path
            if node in visiting:
                return False
            
            if node not in seen:
                seen.add(node)

            visiting.add(node)
            for nei in hSet[node]:
                if nei != parentN:
                    if not dfs(nei, node):
                        return False
            visiting.remove(node)
            return True
        
        for node in range(n):
            if not dfs(node,None):
                return False
            if len(seen) == n:
                connected = True
            seen.clear()
        return True and connected

        