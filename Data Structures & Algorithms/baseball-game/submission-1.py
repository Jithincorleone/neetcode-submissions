class Solution:
    def calPoints(self, operations: List[str]) -> int:
        temp=[]
        net=0
        
        for idx in range(len(operations)):
            if operations[idx] not in ("+","C","D"):
                temp.append(int(operations[idx]))
            if operations[idx] == "+":
                val1=temp[-1]
                val2=temp[-2]
                val3=int(val1)+int(val2)
                temp.append(val3)
            if operations[idx]=="C":
                temp.pop()
            if operations[idx]=="D":
                val=temp[-1]*2
                temp.append(val)
        
        for val in temp:
            net+=val
        
        return net

            



