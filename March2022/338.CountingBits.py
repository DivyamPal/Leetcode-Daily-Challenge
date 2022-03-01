class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        list=[]
        for i in range(num+1):
            if(i>1):
             list.append(bin(i)[2:].count('1'))
            else:
             list.append(i)
        return list