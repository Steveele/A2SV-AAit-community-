       answer=[]
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                if (nums[j] > nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                else:
                    continue
        for i in range(len(nums)):
            if (nums[i]==target):
                answer.append(i)
        return answer