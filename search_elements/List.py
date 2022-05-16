from search_elements.Data_Structures import Data_Structure
import time
import random


class Lista(Data_Structure):

    def search_element_list(self):
        lista = [i for i in range(self.numerical_limit)]
        time_begin_list = time.time()
        result = None
        for index in lista:
            if lista[index] == random.randint(0, self.numerical_limit):
                result = lista[index]
                break
        time_finish_list = time.time()
        temporal_dif_list = 1e6 * (time_finish_list - time_begin_list)
        print('The list has wasted {} microsecs searching an element'.format(temporal_dif_list))
        return result
