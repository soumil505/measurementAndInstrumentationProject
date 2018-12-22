import numpy as np


class Filter:
    def __init__(self, n):
        self.n = n

    def real_time(self, list):
        list_length = len(list)
        if list_length < self.n:
            list2 = np.append(np.zeros(self.n - list_length) + list[0], list)
        else:
            list2 = list[(list_length - self.n):]
        list[-1] = np.average(list2)
        return list


