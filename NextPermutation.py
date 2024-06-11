class Solution(object):
    def mergeSort(self, arr):
        if len(arr) > 1:
            m = len(arr)//2
            l = arr[:m]
            r = arr[m:]
            self.mergeSort(l)
            self.mergeSort(r)
            i = j = k = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    arr[k] = l[i]
                    i += 1
                else:
                    arr[k]=r[j]
                    j +=1
            
                k = k + 1      
            while i < len(l):
                arr[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                arr[k] = r[j]
                j +=1
                k +=1


    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        isInter = False

        for i in range(len(nums) - 1, 0 , -1):
            if nums[i] > nums[i-1]:
                isInter = True
                start = i-1
                break
        if isInter:
            for j in range(start + 1, len(nums)):
                if nums[j] < nums[start]:
                    nums[start], nums[j -1] = nums[j-1],nums[start]
                    break
            sort_arr = nums[start + 1:]
            self.mergeSort(sort_arr)
            
            return nums[:start + 1] + sort_arr

        else:
            return nums[::-1]
        
    

c = Solution()
# arr = [1,5,8,4,7,6,5,3,1]
arr = [3, 2, 1]
# arr = [1,1,5]
print(c.nextPermutation(arr))