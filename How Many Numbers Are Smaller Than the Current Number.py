
        
     answer=[]   
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if (nums[i]==nums[j]):
                    continue
                elif (nums[i]>nums[j]):
                    count+=1
            answer.append(count)       
        return answer