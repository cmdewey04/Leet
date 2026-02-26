# Last updated: 2/26/2026, 2:21:42 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        m = len(matrix) - 1
4        n = len(matrix[0]) - 1
5
6        left_m, right_m = 0, m
7        left_n, right_n = 0, n
8
9        while left_m <= right_m and left_n <= right_n:
10            mid_m = (left_m + right_m) // 2
11            mid_n = (left_n + right_n) // 2
12
13            prospect = matrix[mid_m][mid_n]
14            if prospect == target:
15                return True
16            elif prospect < target:
17                # Stay in Pod
18                if target <= matrix[mid_m][n]:
19                    # left_m = mid_m + 1
20                    left_m = mid_m
21                    right_m = mid_m
22                    left_n = mid_n + 1
23                else:
24                    # Jump to next Pod
25                    left_m = mid_m + 1
26
27            else:
28                # Stay in Pod
29                if target >= matrix[mid_m][0]:
30                    left_m = mid_m
31                    right_m = mid_m
32                    right_n = mid_n - 1
33                else:
34                    # Jump to next Pod
35                    right_m = mid_m - 1
36
37        return False
38