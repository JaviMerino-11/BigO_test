import random
import time


class Data_Structure(object):
    def __init__(self, structure_type: str, numerical_limit: int):
        self.structure_type = structure_type
        self.numerical_limit = numerical_limit

    def time_medition_no_decorator(self, function):
        start_medition = time.time()
        function()
        stop_medition = time.time()
        temporal_dif_list = 1e6 * (stop_medition - start_medition)
        print('The %s has wasted %i microsecs searching an element' % (self.structure_type, temporal_dif_list))

    # def time_medition(self, function):
    #     def wrapper(*args, **kwargs):
    #         start_medition = time.time()
    #         result = function(*args, **kwargs)
    #         stop_medition=time.time()
    #         temporal_dif_list = 1e6 * (stop_medition - start_medition)
    #         print('The %s has wasted %i microsecs searching an element' % (self.structure_type, temporal_dif_list))
    #         return result
    #
    #     return wrapper
