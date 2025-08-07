class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.seg = [-1] * (2 * self.size)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, idx, l, r):
        if l == r:
            self.seg[idx] = data[l]
        else:
            m = (l + r) // 2
            self.build(data, 2 * idx, l, m)
            self.build(data, 2 * idx + 1, m + 1, r)
            self.seg[idx] = max(self.seg[2 * idx], self.seg[2 * idx + 1])

    def search(self, idx, l, r, k):
        if self.seg[idx] < k:
            return -1
        if l == r:
            self.seg[idx] = -1
            return l
        m = (l + r) // 2
        if self.seg[2 * idx] >= k:
            pos = self.search(2 * idx, l, m, k)
        else:
            pos = self.search(2 * idx + 1, m + 1, r, k)
        self.seg[idx] = max(self.seg[2 * idx], self.seg[2 * idx + 1])
        return pos


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        seg = SegmentTree(baskets)
        unplaced = 0
        for fruit in fruits:
            if seg.search(1, 0, n - 1, fruit) == -1:
                unplaced += 1
        return unplaced