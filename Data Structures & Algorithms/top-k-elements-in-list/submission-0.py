class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        top_two = [num[0] for num in freq.most_common(k)]     
        return top_two 