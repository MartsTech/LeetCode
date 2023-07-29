class Solution:
    # O(n*log(n)) time | O(n) space
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = [0] * len(spells)
        potions.sort()
        max_potion = potions[-1]
        for i, spell in enumerate(spells):
            min_potion = (success + spell - 1) // spell
            if min_potion > max_potion:
                continue
            index = bisect_left(potions, min_potion)
            result[i] = len(potions) - index
        return result