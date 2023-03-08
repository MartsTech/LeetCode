class Solution:
    # O(nlogk) time | O(n) space
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = {}
        for word in words:
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1
        max_heap = []
        for word, freq in freqs.items():
            heappush(max_heap, (-freq, word))
        result = []
        for _ in range(k):
            _, word = heappop(max_heap)
            result.append(word)
        return result