class Data_Structure(object):
    def __init__(self, structure_type: str, numerical_limit: int):
        self.structure_type = structure_type
        self.numerical_limit = numerical_limit
        self._data = self._create_data()
        self.cocient = round(self.numerical_limit / 10)

    def _get_data_type(self):
        raise NotImplementedError

    def _create_data(self):
        return self._get_data_type()(range(self.numerical_limit))
