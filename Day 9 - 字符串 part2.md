#  [151.翻转字符串里的单词](https://leetcode.cn/problems/reverse-words-in-a-string/) 

![题目](jpgs/151.jpg)


思路
1. 注意string 和 list 转换
2. 直接转换，或者用双指针
3. 双指针注意return 在while 以外

  The solution can be found in the [leetcode541.py](codes/leetcode541.py) file.

```python
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

```
#  [卡码网：55.右旋转字符串](https://kamacoder.com/problempage.php?pid=1065) 

![题目](jpgs/kama55.jpg)

思路
1. 
 



```python

```
 










# References

1. **DAY 8 任务**. [https://docs.qq.com/doc/DUGdsY2JFaFhDRVZH](https://docs.qq.com/doc/DUGdsY2JFaFhDRVZH).  