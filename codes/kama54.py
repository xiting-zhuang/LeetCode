class Solution:
    def change(self, s: str) -> str:
        """
        Replace all digits in the input string with the word 'number'.

        Args:
        s (str): The input string.

        Returns:
        str: The modified string with all digits replaced by 'number'.
        """
        lst = list(s)  # Convert the string to a list of characters
        for i in range(len(lst)):  # Iterate over the list by index
            if lst[i].isdigit():  # Check if the character is a digit
                lst[i] = "number"  # Replace the digit with the string "number"
        return ''.join(lst)  # Join the list back into a string

# Example usage:
sol = Solution()
s = "hello123world"
modified_string = sol.change(s)
print(modified_string)  # Output: "hellonumbernumbernumberworld"