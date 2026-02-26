# Last updated: 2/26/2026, 1:36:36 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Map each course to its prereqs
        sched = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            sched[crs].append(pre)
        
        #Current list of seen courses on path
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if not sched[crs]:
                return True

            visiting.add(crs)
            for nei in sched[crs]:
                if not dfs(nei):
                    return False
            visiting.remove(crs)
            sched[crs] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
