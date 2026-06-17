class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:



        if "0000" in deadends:
            return -1

        q=deque(["0000"])
        dead=set(deadends)
        visited={"0000"}
        level=0
        while q:
            
            for i in range(len(q)):
                curr=q.popleft()
                if curr == target:
                    return level
                for i in range(4):
                   digit =int(curr[i])
                   up=(digit+1)%10
                   nxt = curr[:i] +str(up) +curr[i+1:]
                   if (nxt not in dead and nxt not in visited):
                    visited.add(nxt)
                    q.append(nxt)
                   
                   down=(digit-1)%10
                   nxt = curr[:i] +str(down) +curr[i+1:]
                   if (nxt not in dead and nxt not in visited):
                    visited.add(nxt)
                    q.append(nxt)
            level+=1   

        return -1