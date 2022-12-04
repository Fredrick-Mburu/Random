#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
class NumberTwistes:
    def __init__(self, MinRange,  MaxRange, Count) -> None:
        self.MinRange = MinRange
        self.MaxRange = MaxRange
        self.Count = Count

    def Number_Spinners_And_Spinners(self):
        random_nums = random.sample(range(self.MinRange, self.MaxRange), self.Count)
        print(random_nums)
rand_nums = NumberTwistes(10000,2950000,75)
rand_nums.Number_Spinners_And_Spinners()

