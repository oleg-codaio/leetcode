#!/usr/bin/env python
#
# Given an absolute path for a file (Unix-style), simplify it.
#
# LeetCode Runtime: 68 ms
# Author: oleg@osv.im

import sys

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = filter(None, path.split('/'))
        stack = []
        for part in path:
            if part == '..':
                if stack:
                    stack.pop()
            elif part != '.':
                stack.append(part)
        return '/' + '/'.join(stack)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print Solution().simplifyPath(sys.argv[1])

