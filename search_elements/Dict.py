from search_elements.Data_Structures import Data_Structure
import time
import random


class Dict(Data_Structure):

    def search_element_dict(self):
        values = ['value1']
        mydict = {"key " + str(i): values[0] for i in range(self.numerical_limit)}
        for i in range(self.numerical_limit):
            mydict['key' + str(i)] = random.randrange(self.numerical_limit)
        key_target = 'key {}'.format(random.randint(0, self.numerical_limit))
        time_begin_dict = time.time()
        dicc_value = mydict.get(key_target)
        time_finish_dict = time.time()
        temporal_dif_list = 1e6 * (time_finish_dict - time_begin_dict)
        print('The dict has wasted {} microsecs searching an element'.format(temporal_dif_list))
        return dicc_value
