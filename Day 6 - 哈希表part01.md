
# [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/)

![题目](jpgs/242.jpg)

Given two strings, s and t, determine if t is an anagram of s. Return true if it is, and false otherwise.

An anagram is created by rearranging the letters of a different word or phrase, using all the original letters exactly once.

 
Example 1:
	•	Input: s = "anagram", t = "nagaram"
	•	Output: true

Example 2:

	•	Input: s = "rat", t = "car"
	•	Output: false


### 思路

解决方案详见 [valid_anagram.py](codes/valid_anagram.py) 文件。
```python
 

 
```

# [349. 两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/)

![题目](jpgs/349.jpg)

### 思路
1. 使用 set 来存储第一个数组中的元素，然后遍历第二个数组以找到交集。
2. set 可以高效地判断元素是否存在，时间复杂度为 O(1)。

解决方案详见 [intersection_of_two_arrays.py](codes/intersection_of_two_arrays.py) 文件。

```python
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)
```

# [202. 快乐数](https://leetcode.cn/problems/happy-number/)

![题目](jpgs/202.jpg)

### 思路
1. 使用 set 来检测循环，以避免无限循环。
2. 每次计算当前数字的平方和，判断是否已经出现过。

解决方案详见 [happy_number.py](codes/happy_number.py) 文件。

```python
def isHappy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(x) ** 2 for x in str(n))
    return n == 1
```

# [1. 两数之和](https://leetcode.cn/problems/two-sum/)

![题目](jpgs/1.jpg)

### 思路
1. 使用字典（哈希表）来存储每个数字及其对应的索引。
2. 遍历数组，对于每个数字检查其对应的差值是否在字典中。

解决方案详见 [two_sum.py](codes/two_sum.py) 文件。

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    for i, num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], i]
        num_to_index[num] = i
```

# References

1. **DAY 6 任务**. [https://docs.qq.com/doc/DUEtFSGdreWRuR2p4](https://docs.qq.com/doc/DUEtFSGdreWRuR2p4).
