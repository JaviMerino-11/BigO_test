from search_elements.Data_Structures import Data_Structure
from search_elements.time_decorator import time_medition

import random


class Dict(Data_Structure):

    @time_medition
    def search_element_dict(self):
        values = ['value1']
        mydict = {"key " + str(i): values[0] for i in range(self.numerical_limit)}
        for i in range(self.numerical_limit):
            mydict['key' + str(i)] = random.randrange(self.numerical_limit)
        key_target = 'key {}'.format(random.randint(0, self.numerical_limit))
        dicc_value = mydict.get(key_target)
        return dicc_value
