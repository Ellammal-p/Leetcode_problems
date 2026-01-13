class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close_sum=nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1

            while left<right:
                curr_sum=nums[i]+nums[left]+nums[right]

                if abs(curr_sum-target) < abs(close_sum-target):
                    close_sum=curr_sum
                
                if curr_sum<target:
                    left+=1
                elif curr_sum>target:
                    right-=1
                else:
                    return curr_sum
        return close_sum
