"""
Cell
"""
import copy

class Cell:
    cell_type = ''
    instance = ''
    delay_name = ''         # Absolute or something
    delay = []

    def __init__(self, meta, data):
        self.cell_type, self.instance, self.delay_name = meta
        self.delay = copy.deepcopy(data)
