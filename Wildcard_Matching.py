class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        
        #base case, when the string and pattern are empty
        
        #need a 2D dp, initialize a matrix with size(len(s) X len(pattern))
        dp = [[False for x in range(len(p)+1)] for y in range(len(s)+1)] 
        
        #if the string is empty and the pattern too
        dp[0][0] = True
               
        #the first row with [0][j]
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
                
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                
                #case when current characters in the string and pattern match
                #if we see a '?' then same value as diagnol
                
                if s[i-1] == p[j-1] or p[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                    
                #case when the pattern has a '*', we have two situations
                #either to consider the '*' as empty, then we go left
                #or we consider '*' to be any character, so same as the string
                
                elif p[j-1] =='*':
                    dp[i][j]= dp[i][j-1] or dp[i-1][j]
        
                #if there is no match 
                else:
                    dp[i][j] = False 
                
        return dp[len(s)][len(p)]; 
