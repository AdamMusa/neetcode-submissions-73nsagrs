class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Step 2: Build [frequency, number] pairs
        pairs = []

        for number, count in frequency.items():
            pairs.append([count, number])

        # Step 3: Sort by frequency (ascending)
        pairs.sort()

        # Step 4: Take the k most frequent numbers
        result = []

        for _ in range(k):
            count, number = pairs.pop()
            result.append(number)

        return result