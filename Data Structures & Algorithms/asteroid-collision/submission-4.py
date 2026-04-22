class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[asteroids[0]]
        for i in range(1,len(asteroids)):
            while res and  res[-1] > 0 and asteroids[i] < 0:
                if abs(asteroids[i])>abs(res[-1]):
                    res.pop()
                    continue
                elif abs(asteroids[i])==abs(res[-1]):
                    res.pop()
                break
            else:
                res.append(asteroids[i])
        return res

