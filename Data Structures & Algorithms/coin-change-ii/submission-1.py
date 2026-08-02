class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo={}
        def fun(ind,tar):
            if tar==amount:
                return 1
            if ind>=len(coins) or tar>amount:
                return 0
            if (ind,tar) in memo:
                return memo[(ind,tar)]
            #pick
            pick = fun(ind,tar+coins[ind])
            #not pick
            nt_pick = fun(ind+1,tar)
            memo[(ind,tar)] = pick + nt_pick
            return memo[(ind,tar)]
        return fun(0,0)