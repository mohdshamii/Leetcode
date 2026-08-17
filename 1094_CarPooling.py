class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001

        for passengers, start, end in trips:
            stops[start] += passengers
            stops[end] -= passengers

        current = 0

        for passengers in stops:
            current += passengers
            if current > capacity:
                return False

        return True
