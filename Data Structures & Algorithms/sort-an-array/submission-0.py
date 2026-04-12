class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        def merge(low,mid,high,nums):
            left,right = nums[low:mid+1],nums[mid+1:high+1]
            i,j,k=low,0,0

            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    nums[i]=left[j]
                    j+=1
                else:
                    nums[i]=right[k]
                    k+=1
                i+=1
            
            while j<len(left):
                nums[i]=left[j]
                j+=1
                i+=1
            
            while k<len(right):
                nums[i]=right[k]
                k+=1
                i+=1

        def sortIt(low, high,nums):
            if low>=high:
                return 
            mid= (low + high)//2

            sortIt(low,mid,nums)
            sortIt(mid+1,high,nums)
            merge(low,mid,high,nums)




        n=len(nums)
        sortIt(0,n-1,nums)
        return nums
        