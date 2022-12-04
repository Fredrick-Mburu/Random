#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
class MoversGenerator:
    def __init__(self, MinRange,  MaxRange, Count) -> None:
        self.MinRange = MinRange
        self.MaxRange = MaxRange
        self.Count = Count

    def Pumping_Random_Numbers(self):
        random_nums = random.sample(range(self.MinRange, self.MaxRange), self.Count)
        print(random_nums)
rand_nums = MoversGenerator(0,1000,5)
rand_nums.Pumping_Random_Numbers()

