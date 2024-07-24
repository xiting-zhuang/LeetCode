class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters in the current 2k block
            res.append(s[i:i+k][::-1])
            # Append the remaining characters in the current 2k block as is
            res.append(s[i+k:i+2*k])
        return ''.join(res)
    

# Example usage:
sol = Solution()
s1 = "goodmorning"
k = 2
result = sol.reverseStr(s1, k)
print(result)  # Output should be the modified string after applying the logic