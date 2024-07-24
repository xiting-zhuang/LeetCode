from typing import List
 
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        # Split the string into words, reverse the list of words, and join them back together
        reversed_words = ' '.join(reversed(s.split()))
        return reversed_words

    def reverseTwopoint(self, s: str) -> str:
        words = s.split()
        l , r = 0 , len(words) - 1
        while l < r:
            words[l] , words[r] = words[r] , words[l]
            l += 1 
            r -= 1 
        return " ".join(words) 

# Example usage
solution = Solution()
output1 = solution.reverseWords("   Hello world!   This is a test.   ")
print(output1)  


output2 = solution.reverseTwopoint("   Hello world!   This is a test.   ")
print(output2)  
