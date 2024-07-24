#  [151.翻转字符串里的单词](https://leetcode.cn/problems/reverse-string/) 

![题目](jpgs/344.jpg)


思路
1. 移除空格
2. 翻转string(直接翻转或者用双指针)
3. 注意 string 和 list 的data type来回转换


  The solution can be found in the [leetcode151.py](codes/leetcode151.py) file.

```python
    def reverseWords(self, s: str) -> str:
        s = s.strip()
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
 
#  [151.翻转字符串里的单词](https://leetcode.cn/problems/reverse-string/) 

![题目](jpgs/344.jpg)


思路
1. 移除空格
2. 翻转string(直接翻转或者用双指针)
3. 注意 string 和 list 的data type来回转换


  The solution can be found in the [leetcode151.py](codes/leetcode151.py) file.

```python
  
```





# References

1. **DAY 9 任务**. [https://docs.qq.com/doc/DUHVXSnZNaXpVUHN4](https://docs.qq.com/doc/DUHVXSnZNaXpVUHN4).  