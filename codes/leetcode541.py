def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        # Move pointers
        left += 1
        right -= 1

# Example usage:
s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(s1)  # Output: ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(s2)  # Output: ["h", "a", "n", "n", "a", "H"]