from search_elements.Data_Structures import Data_Structure
from search_elements.time_decorator import time_medition

import random


class Set(Data_Structure):

    @time_medition
    def search_element_set(self):
        set = {i for i in range(self.numerical_limit)}
        set_target = random.randint(0, self.numerical_limit) in set
        set_value = set_target
        return set_value
