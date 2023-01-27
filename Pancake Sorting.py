class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        out=[]
        leng=len(arr)

        for i in range(len(arr)):
            maximum=max(arr[:leng-i])
            max_index=arr.index(maximum)+1
            arr[:max_index]=reversed(arr[:max_index-i])
            out.append(max_index)

            arr[:leng-i]=reversed(arr[:leng-i])
            out.append(leng-i)
        return out


        