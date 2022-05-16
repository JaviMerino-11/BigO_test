from search_elements.Data_Structures import Data_Structure
from search_elements.time_decorator import time_medition

import random


class Lista(Data_Structure):

    @time_medition
    def search_element_list(self):
        lista = [i for i in range(self.numerical_limit)]
        result = None
        for index in lista:
            if lista[index] == random.randint(0, self.numerical_limit):
                result = lista[index]
                break
        return result
