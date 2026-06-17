class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = [0] * (len(s) + 1)

        for i, ch in enumerate(s, 1):
            current_length = lengths[i - 1]

            if "a" <= ch <= "z":
                lengths[i] = current_length + 1
            elif ch == "*":
                lengths[i] = max(0, current_length - 1)
            elif ch == "#":
                lengths[i] = current_length * 2
            else:
                lengths[i] = current_length

        if k >= lengths[-1]:
            return "."

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            before_length = lengths[i]
            after_length = lengths[i + 1]

            if "a" <= ch <= "z":
                if k == after_length - 1:
                    return ch
            elif ch == "#":
                if before_length > 0:
                    k %= before_length
            elif ch == "%":
                if before_length > 0:
                    k = before_length - 1 - k

        return "."