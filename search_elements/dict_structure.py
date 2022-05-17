from search_elements.data_structures import Data_Structure
from search_elements.time_medition import time_medition

import random


class Dict_Structure(Data_Structure):

    @time_medition
    def search_element_dict(self):
        result = None
        target_key = random.randint(0, self.numerical_limit)
        if target_key in self._data:
            result = target_key
        return result

    def _get_data_type(self):
        return dict

    def _create_data(self):
        return {key_dict: None for key_dict in range(self.numerical_limit)}
