class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        
        if not fruits:
            return 0
            
        window_start = 0
        max_length = 0
        fruit_counts = {}

        # The 'window_end' pointer expands the window to the right.
        for window_end in range(len(fruits)):
            right_fruit = fruits[window_end]
            fruit_counts[right_fruit] = fruit_counts.get(right_fruit, 0) + 1
          
            while len(fruit_counts) > 2:
                left_fruit = fruits[window_start]
                fruit_counts[left_fruit] -= 1
                if fruit_counts[left_fruit] == 0:
                    del fruit_counts[left_fruit]
                window_start += 1
          
            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length