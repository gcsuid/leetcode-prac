class solution:
    def boatsave(self, people: list[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            total = people[left] + people[right]
            if total <= limit:
                l += 1
                r -= 1
                count += 1
            else:
                r -= 1
                count += 1
        return boats
