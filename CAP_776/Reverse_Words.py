class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        
        N = S.split('.')
        re_N= N[::-1]
        result = '.'.join(re_N)
        
