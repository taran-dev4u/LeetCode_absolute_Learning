from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        highest_altitude = 0

        for change_in_altitude in gain:
            current_altitude += change_in_altitude
            if current_altitude > highest_altitude:
                highest_altitude = current_altitude

        return highest_altitude