from search_elements.data_structures import Data_Structure
from search_elements.time_medition import time_medition

import random


class List_Structure(Data_Structure):

    @time_medition
    def search_element_list(self):
        result = None
        target_element = random.randint(0, self.numerical_limit)
        if target_element in self._data:
            result = target_element
        return result

    def _get_data_type(self):
        return list
