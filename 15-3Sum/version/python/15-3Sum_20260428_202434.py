# Last updated: 4/28/2026, 8:24:34 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        arr = []
4        seen = set()
5        nums.sort()
6        for i in range(len(nums)-2):
7            if nums[i] in seen:
8                continue
9            seen.add(nums[i])
10            #target = -num
11            l,r = i+1, len(nums)-1
12            while l<r:
13                res = nums[l] + nums[r] + nums[i]
14                # if res < target:
15                #     l+=1
16                # elif res > target:
17                #     r-=1
18                # else:
19                #     arr.append([num, nums[l], nums[r]])
20                #     break
21                if res == 0:
22                    arr.append([nums[i], nums[l], nums[r]])
23                    l+=1
24                    r-=1
25                    while l<r and nums[l] == nums[l-1]:
26                        l+=1
27                elif res < 0:
28                    l+=1
29                else:
30                    r-=1 
31
32        return arr
33
34                