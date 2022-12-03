#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
class RandomGenerator:
    def __init__(self, MinRange,  MaxRange, Count) -> None:
        self.MinRange = MinRange
        self.MaxRange = MaxRange
        self.Count = Count

    def Populate_Random_Numbers(self):
        random_nums = random.sample(range(self.MinRange, self.MaxRange), self.Count)
        print(random_nums)
rand_nums = RandomGenerator(200,1000,9)
rand_nums.Populate_Random_Numbers()

