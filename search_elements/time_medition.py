import time


def time_medition(function_parameter):
    def wrapper(self):
        start_medition = time.time()
        function_parameter(self)
        stop_medition = time.time()
        temporal_dif_list = 1e6 * (stop_medition - start_medition)
        print('The %s has wasted %i microsecs searching %i elements' % (
            self.structure_type, temporal_dif_list, self.cocient))

    return wrapper
