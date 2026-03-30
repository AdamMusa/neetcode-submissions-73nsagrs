class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        flets = 0
        prev_time = 0
        for p,spd in cars:
            time = (target - p) / spd
            if time > prev_time:
                flets +=1
                prev_time = time
        return flets