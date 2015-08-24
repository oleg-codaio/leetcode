#!/usr/bin/env python
#
# Given a string s and a dictionary of words dict, determine if s can be
# segmented into a space-separated sequence of one or more dictionary words.
#
# LeetCode Runtime: 40 ms (beats 99.40% of Python coders)
# Author: oleg@osv.im

import sys

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s:
            return True
        if not wordDict:
            return False

        minWord = len(min(wordDict, key=len))
        maxWord = len(max(wordDict, key=len))

        wordDict = set(filter(lambda x: len(x) <= len(s), wordDict))
        # True if s[:i] is breakable
        mem = [False] * (len(s) + 1)
        mem[0] = True

        for i in xrange(len(s)):
            if mem[i] is False:
                continue

            maxWordI = min(maxWord + i + 1, len(s))
            for j in xrange(minWord + i, maxWordI + 1):
                if mem[j] is False:
                    mem[j] = s[i:j] in wordDict
                    if j == len(s) and mem[j]:
                        return True

        return False

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print Solution().wordBreak(sys.argv[1],
                [x[1:-1] for x in sys.argv[2][1:-1].split(',')])

