from search_elements.data_structures import Data_Structure
from search_elements.time_medition import time_medition

import random


class Set_Structure(Data_Structure):

    @time_medition
    def search_element_set(self):
        list_results = [None] * self.cocient
        for targets in range(self.cocient):
            target_element = (random.randint(0, self.numerical_limit))
            if target_element in self._data:
                list_results[targets] = target_element
            return list_results

    def _get_data_type(self):
        return set
