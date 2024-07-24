from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the characters in the list s in-place.
        
        Args:
        s (List[str]): A list of characters representing the string to be reversed.
        
        Returns:
        None: The list s is modified in-place to reverse its characters.
        """
        # Initialize two pointers: l at the start, r at the end of the list
        l, r = 0, len(s) - 1

        # Loop until the two pointers meet in the middle
        while l < r:
            # Swap the characters at l and r indices
            s[l], s[r] = s[r], s[l]
            # Move the left pointer towards the center
            l += 1
            # Move the right pointer towards the center
            r -= 1
        return s 
 
# Example usage:
sol = Solution()
s1 = ["h", "e", "l", "l", "o"]
sol.reverseString(s1)
print(s1)  # Output: ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
sol.reverseString(s2)
print(s2)  # Output: ["h", "a", "n", "n", "a", "H"]