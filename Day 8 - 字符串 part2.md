#  [344.反转字符串](https://leetcode.cn/problems/reverse-string/) 

![题目](jpgs/344.jpg)


思路
1. 空间复杂度o(1),因此不能使用额外的空间
2. 利用双指针, 而且该方法已经不需要判断奇偶数


  The solution can be found in the [leetcode541.py](codes/leetcode541.py) file.

```python
def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        # Move pointers
        left += 1
        right -= 1
```


#  [ 541. 反转字符串II](https://leetcode.com/problems/reverse-string-ii/description/) 

![题目](jpgs/541.jpg)

思路
1. range 函数with 3 arguments （start, stop, step)
2. .append() 是 list Method. 合并list的item
3. .join() 是 string Method. 合并转换list 成 string



```python
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

```



#  [ 卡码网：54.替换数字 ](https://kamacoder.com/problempage.php?pid=1064) 

![题目](jpgs/kama54.jpg)

思路： 
1. string是immutable，转换成list操作
 
 
```python
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


```


# References

1. **DAY 8 任务**. [https://docs.qq.com/doc/DUGdsY2JFaFhDRVZH](https://docs.qq.com/doc/DUGdsY2JFaFhDRVZH).  