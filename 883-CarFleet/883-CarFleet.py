# Last updated: 2/26/2026, 1:36:24 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # cars = []
        # stack = []
        # for i in range(len(position)):
        #     cars.append([position[i],speed[i]])
        # cars.sort(reverse=True)
    
        # for car in cars:
        #     time = (target - car[0]) / car[1]
        #     if stack:
        #         if stack[-1][0] >= time:
        #             stack[-1].append(time)
        #         else:
        #             stack.append([time])
        #     else:
        #         stack.append([time])
        
        # return len(stack)




        #create an array combining poisition and speed for each car
        #calculate time to target for each car target - position / speed
        #add those onto the stack, if the current car is less than or equal to time for car ahead, add it to fleet

        stack = []
        cars = [[p,s] for p, s in zip(position,speed)]
        cars.sort(reverse=True)
        for p,s in cars:
            # stack.append((target-p)/s)
            time = (target - p) / s
            # if len(stack) >= 2 and stack[-1] <= stack[-2]:
            #     stack.pop()
            if len(stack) >=1 and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        
        return len(stack)