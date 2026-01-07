class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal=[]
        for i in range(rowIndex+1):
            row=[]
            for j in range(i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    privious=pascal[i-1]
                    row.append(privious[j]+privious[j-1])
            pascal.append(row)
        last=pascal[-1]
        return last
                    