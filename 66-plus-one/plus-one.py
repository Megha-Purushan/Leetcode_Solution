class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):

            # If digit is less than 9, simply add 1
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9, make it 0 and continue
            digits[i] = 0

        # If all digits were 9
        return [1] + digits
        
        