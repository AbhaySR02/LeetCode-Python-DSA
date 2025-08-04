from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        if n == 0:
            return 0

        # Using direct access is cleaner than creating new lists
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + fruits[i][1]

        def get_window_sum(left_idx: int, right_idx: int) -> int:
            if left_idx > right_idx:
                return 0
            return prefix_sum[right_idx + 1] - prefix_sum[left_idx]

        max_collected_fruits = 0
        left_idx = 0

        for right_idx in range(n):
            # Calculate cost for the current window [left_idx, right_idx]
            left_pos = fruits[left_idx][0]
            right_pos = fruits[right_idx][0]
            dist = right_pos - left_pos
            cost = dist + min(abs(startPos - left_pos), abs(startPos - right_pos))
            
            # --- WHILE LOOP (Shrinks the window) ---
            # If cost is too high, move the left pointer to the right
            while cost > k:
                left_idx += 1
                if left_idx > right_idx:
                    break
                
                # Recalculate cost for the new, smaller window
                left_pos = fruits[left_idx][0]
                dist = right_pos - left_pos
                cost = dist + min(abs(startPos - left_pos), abs(startPos - right_pos))
            
            # --- AFTER THE WHILE LOOP ---
            # Now the window is valid (cost <= k). Calculate fruits and update max.
            current_fruits = get_window_sum(left_idx, right_idx)
            max_collected_fruits = max(max_collected_fruits, current_fruits)
            
        return max_collected_fruits