# Last updated: 4/25/2026, 2:49:28 PM
1class Solution:
2    def thirdMax(self, nums: List[int]) -> int:
3       
4
5        numDis = 0
6        unique = set(nums)
7        new = []
8        if len(unique) >= 3:
9            for num in unique:
10                new.append(num)
11            new.sort()
12            return new[-3]
13    
14        return max(nums)
15
16        
17        