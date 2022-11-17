class Solution:
    def sortSentence(self, s: str) -> str:
        list1=s.split()
        list2=[]
        for j in range(len(list1)):
            list2.append(j)
        for i in list1:
            listItems=i
            lastChar=int(listItems[-1])
            list2[lastChar-1]=listItems[0:len(i)-1]
        delimiter = ' '
        return delimiter.join(list2)
      