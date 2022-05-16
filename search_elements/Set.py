from search_elements.Data_Structures import Data_Structure
import time
import random


class Set(Data_Structure):

    def search_element_set(self):
        set = {i for i in range(self.numerical_limit)}
        time_begin_set = time.time()
        set_target = random.randint(0, self.numerical_limit) in set
        set_value = set_target
        time_finish_set = time.time()
        temporal_dif_list = 1e6 * (time_finish_set - time_begin_set)
        print('The set has wasted {} microsecs searching an element'.format(temporal_dif_list))
        return set_value
