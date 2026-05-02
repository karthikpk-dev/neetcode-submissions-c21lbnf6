class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        low=0
        high=mountainArr.length()-1
        peak=-1
        def bs1(low,high):
            
            while low<=high:
                mid=low+(high-low)//2
                if mountainArr.get(mid) == target:
                    return mid
                if mountainArr.get(mid) < target:
                    low=mid+1
                else:
                    high=mid -1
            return -1
        def bs2(low,high):
            
            while low<=high:
                mid=low+(high-low)//2
                if mountainArr.get(mid) == target:
                    return mid
                if mountainArr.get(mid) > target:
                    low=mid+1
                else:
                    high=mid -1
            return -1
        while low<high:
            mid=(low+high)//2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                low=mid+1
            else:
                high=mid
        peak=low
        if  mountainArr.get(peak) == target:
            return peak          
        return bs1(0,peak-1) if bs1(0,peak-1)!=-1 else bs2(peak+1,mountainArr.length()-1)