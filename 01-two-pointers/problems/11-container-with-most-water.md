# 11. Container With Most Water

**Difficulty:** Medium

**Topics:** Array, Two Pointers, Greedy

---

### Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the $i^{th}$ line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.

### Examples

**Example 1:**
- **Input:** `height = [1,8,6,2,5,4,8,3,7]`
- **Output:** `49`
- **Explanation:** The max area is formed between indices 1 and 8 (heights 8 and 7). Area = $min(8, 7) \times (8 - 1) = 7 \times 7 = 49$.

**Example 2:**
- **Input:** `height = [1,1]`
- **Output:** `1`

### Constraints
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

### Two Pointers Approach

The strategy is to start with the widest possible container (pointers at both ends) and greedily move the pointer pointing to the shorter line inward.

1. **Why move the shorter line?** The area is constrained by the shorter line. Moving the taller line inward can only decrease the width without increasing the bottleneck height. Moving the shorter line is the only way to potentially find a taller line that compensates for the loss in width.

```python
def maxArea(height: List[int]) -> int:
    L, R = 0, len(height) - 1
    max_area = 0
    
    while L < R:
        width = R - L
        # Calculate area using the shorter boundary
        if height[L] < height[R]:
            max_area = max(max_area, height[L] * width)
            L += 1
        else:
            max_area = max(max_area, height[R] * width)
            R -= 1
            
    return max_area
```

- **Time Complexity:** $O(n)$ - Single pass through the array.
- **Space Complexity:** $O(1)$ - Constant extra space.
