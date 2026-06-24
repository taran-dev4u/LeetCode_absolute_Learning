from typing import List


class Solution:
    MOD = 10 ** 9 + 7

    def _multiply_matrix(
        self, left: List[List[int]], right: List[List[int]]
    ) -> List[List[int]]:
        size = len(left)
        product = [[0] * size for _ in range(size)]

        for row in range(size):
            for mid in range(size):
                left_value = left[row][mid]
                if left_value == 0:
                    continue

                for col in range(size):
                    product[row][col] = (
                        product[row][col] + left_value * right[mid][col]
                    ) % self.MOD

        return product

    def _multiply_matrix_vector(
        self, matrix: List[List[int]], vector: List[int]
    ) -> List[int]:
        size = len(matrix)
        result = [0] * size

        for row in range(size):
            total = 0
            for col in range(size):
                total = (total + matrix[row][col] * vector[col]) % self.MOD
            result[row] = total

        return result

    def _apply_power_to_vector(
        self, matrix: List[List[int]], power: int, vector: List[int]
    ) -> List[int]:
        current_matrix = matrix
        current_vector = vector[:]

        while power > 0:
            if power & 1:
                current_vector = self._multiply_matrix_vector(
                    current_matrix, current_vector
                )

            current_matrix = self._multiply_matrix(current_matrix, current_matrix)
            power >>= 1

        return current_vector

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        if n == 1:
            return m
        if n == 2:
            return (m * (m - 1)) % self.MOD

        transition = [[0] * m for _ in range(m)]
        for end_value in range(1, m + 1):
            for start_value in range(1, m + 1):
                # Number of possible middle values smaller than both ends
                transition[end_value - 1][start_value - 1] = (
                    min(end_value, start_value) - 1
                )

        up_length_two = [value - 1 for value in range(1, m + 1)]

        up_length_three = [0] * m
        for end_value in range(1, m + 1):
            count = 0
            for middle_value in range(1, end_value):
                count = (count + (m - middle_value)) % self.MOD
            up_length_three[end_value - 1] = count

        if n % 2 == 0:
            power = (n - 2) // 2
            up_final = self._apply_power_to_vector(
                transition, power, up_length_two
            )
        else:
            power = (n - 3) // 2
            up_final = self._apply_power_to_vector(
                transition, power, up_length_three
            )

        total_up = sum(up_final) % self.MOD

        # Up-ending and down-ending arrays are symmetric.
        return (2 * total_up) % self.MOD