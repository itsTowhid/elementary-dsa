# Problems

## Basic 
- [Two Sum](https://leetcode.com/problems/two-sum/)
<!-- colupsible section -->
<details>
<summary>Click to expand!</summary>
<!-- tabbed view for different language solution -->

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
```

```javascript
var twoSum = function(nums, target) {
    let seen = {};
    for (let i = 0; i < nums.length; i++) {
        if (target - nums[i] in seen) {
            return [seen[target - nums[i]], i];
        }
        seen[nums[i]] = i;
    }
    return [];
};
```

```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen;
    for (int i = 0; i < nums.size(); i++) {
        if (seen.find(target - nums[i]) != seen.end()) {
            return {seen[target - nums[i]], i};
        }
        seen[nums[i]] = i;
    }
    return {};
}
``` 
</details>

- [Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- [Palindrome Number](https://leetcode.com/problems/palindrome-number/)
- [Color Sort](https://leetcode.com/problems/sort-colors/)


## Stack
- [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## Binary Search
- [Binary Search](https://leetcode.com/problems/binary-search/)
- [Search Insert Position](https://leetcode.com/problems/search-insert-position/)
- [Find Peak Element](https://leetcode.com/problems/find-peak-element/)

## Linked List
- [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

## Tree
- [Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

## Graph
- [Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
- [Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

## Dynamic Programming
- [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [Coin Change](https://leetcode.com/problems/coin-change/)
- [House Robber](https://leetcode.com/problems/house-robber/)
- [House Robber II](https://leetcode.com/problems/house-robber-ii/)


### Some more interesting problems
- [N Queen](https://leetcode.com/problems/n-queens/)
- [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- [Detonate the Maximum Bombs](https://leetcode.com/problems/detonate-the-maximum-bombs/)

<div style="display: flex; justify-content: space-between;">
    <div style="width: 50%;">

[PREV](step-5.md)

</div>
    <div style="width: 50%; text-align: right;">

[BONUS](step-6.md)
    </div>
</div>