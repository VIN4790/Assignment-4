#!/usr/bin/env python
# coding: utf-8

# In[ ]:

Question 1



# In[ ]:

class Solution:
    def __init__(self,arr1,aar2,arr3):
        self.arr1=arr1
        self.arr2=arr2
        self.arr3=arr3
    def sort_arr(self):
        arr=[]
        for x in self.arr1:
            for y in self.arr2:
                if x==y:
                    for z in self.arr3:
                        if y==z:
                            arr.append(z)
        return arr
# samp1=Solution([1,2,3,4,5],[1,2,5,7,9],[1,3,4,5,8])   
# print(samp1.arr1)
# samp1.sort_arr()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




