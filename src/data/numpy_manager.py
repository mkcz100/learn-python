import numpy as np
import csv
from typing import (
    Any
)


class NumpyManger(object):
    def to_array(self, list) -> Any:
        return np.array(list)

    def load_file(self, file_path) -> Any:
        with open(file_path, 'r') as x:
            sample_data = list(csv.reader(x, delimiter=","))

        return self.to_array(sample_data)
