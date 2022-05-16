import time


class Time:

    def time_medition(self, function):
        start_medition = time.time()
        function()
        stop_medition = time.time()
        temporal_dif_list = 1e6 * (stop_medition - start_medition)
        print('The %s has wasted %i microsecs searching an element' % (self.structure_type, temporal_dif_list))
