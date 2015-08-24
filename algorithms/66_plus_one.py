#!/usr/bin/env python
#
# Given a non-negative number represented as an array of digits, plus one to the
# number. The digits are stored such that the most significant digit is at the
# head of the list.
#
# LeetCode Runtime: 40 ms (beats 100% of Python coders)
# Author: oleg@osv.im

import sys

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(digits) - 1, -2, -1):
            if i == -1:
                digits.insert(0, 1)
            elif digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

        return digits

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print Solution().plusOne(sys.argv[1][1:-1].split(','))

