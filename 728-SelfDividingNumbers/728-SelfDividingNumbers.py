# Last updated: 2/26/2026, 1:36:26 PM
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        # for i in range(left, right+1):
        #     digits = str(i)
        #     if "0" in digits:
        #         continue
        #     count = 0
        #     for num in range(len(digits)):
        #         if i % int(digits[num]) == 0:
        #             count+=1
        #     if count == len(digits):
        #         nums.append(i)
        # return nums

        for i in range(left, right+1):
            n = i
            self_divide = True
            while n > 0:
                digit = n % 10
                if digit == 0 or i % digit != 0:
                    self_divide = False
                    break
                n //= 10
            if self_divide:
                nums.append(i)
        return nums


           

            