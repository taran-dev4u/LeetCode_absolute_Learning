class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Count the needed letters and return the bottleneck value.
        """
        counts = {}

        for character in text:
            if character not in counts:
                counts[character] = 0
            counts[character] += 1

        return min(
            counts.get("b", 0),
            counts.get("a", 0),
            counts.get("l", 0) // 2,
            counts.get("o", 0) // 2,
            counts.get("n", 0),
        )