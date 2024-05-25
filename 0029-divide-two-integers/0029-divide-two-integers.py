class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend <0 ) and (divisor<0):
            return (dividend//divisor if (dividend//divisor <= ((2**31)-1)) else (2**31)-1)
        elif (dividend <0 ) or (divisor<0):
            return (-(abs(dividend)//abs(divisor)) if (-(abs(dividend)//abs(divisor)) > -(2**31)) else -(2**31) )
        else:
            return (dividend//divisor if (dividend//divisor <= (2**31)-1) else (2**31)-1)
        