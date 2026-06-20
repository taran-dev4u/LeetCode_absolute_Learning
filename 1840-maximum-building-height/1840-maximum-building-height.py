from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        points = [[1, 0]]
        points.extend(restrictions)

        found_n = False
        for building_id, _ in points:
            if building_id == n:
                found_n = True
                break

        if not found_n:
            points.append([n, n - 1])

        points.sort()

        for i in range(1, len(points)):
            distance = points[i][0] - points[i - 1][0]
            points[i][1] = min(points[i][1], points[i - 1][1] + distance)

        for i in range(len(points) - 2, -1, -1):
            distance = points[i + 1][0] - points[i][0]
            points[i][1] = min(points[i][1], points[i + 1][1] + distance)

        answer = 0
        for i in range(1, len(points)):
            left_index, left_height = points[i - 1]
            right_index, right_height = points[i]
            distance = right_index - left_index

            best_peak = (left_height + right_height + distance) // 2
            answer = max(answer, best_peak)

        return answer