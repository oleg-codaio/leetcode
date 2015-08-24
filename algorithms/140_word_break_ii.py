#!/usr/bin/env python
#
# Given a string s and a dictionary of words dict, add spaces in s to construct
# a sentence where each word is a valid dictionary word. Return all such possible
# sentences.
#
# LeetCode Runtime: 44 ms (beats 100% of Python coders)
# Author: oleg@osv.im

import sys

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return []

        minWord = len(min(wordDict, key=len))
        maxWord = len(max(wordDict, key=len))

        wordDict = set(filter(lambda x: len(x) <= len(s), wordDict))

        # True if s[:i] is breakable
        mem = [set() for i in range(len(s) + 1)]

        for i in xrange(len(s)):
            if not mem[i] and i is not 0:
                continue

            maxWordI = min(maxWord + i + 1, len(s))
            for j in xrange(minWord + i, maxWordI + 1):
                word = s[i:j]
                if word in wordDict:
                    mem[j].add(word)

        if not mem[len(s)]:
            return []

        words = [(x, 0) for x in mem[len(s)]]
        while True:
            done = True
            num = len(words)
            for i in range(num):
                phrase, spaces = words.pop(0)
                if len(phrase) - spaces is not len(s):
                    done = False

                    prevPhrases = mem[len(s) - len(phrase) + spaces]
                    for prev in prevPhrases:
                        words.append((prev + " " + phrase, spaces + 1))

                    if not prevPhrases:
                        raise Exception('Illegal state!')
                else:
                    words.append((phrase, spaces))

            if done:
                return [x[0] for x in words]

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print Solution().wordBreak(sys.argv[1],
                [x[1:-1] for x in sys.argv[2][1:-1].split(',')])

