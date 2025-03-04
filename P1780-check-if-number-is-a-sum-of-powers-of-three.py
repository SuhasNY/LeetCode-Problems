def solve(n, i):
        if(n==0):
            return True

        while(i <= n):
            if (solve(n-i, i*3) == True):
                return True
            i = i*3

        return False

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = 1
        return solve(n, i)