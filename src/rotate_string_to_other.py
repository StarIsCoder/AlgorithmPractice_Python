#  A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
#  For example, if A = 'abcde', then it will be 'bcdea' after one shift on A.
#  Return True if and only if A can become B after some number of shifts on A.


class Solution(object):
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A + A
