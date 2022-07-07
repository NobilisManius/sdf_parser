"""
Cell
"""

class Cell:
    cell_type = ''
    instance = ''
    delay_name = ''         # Absolute or something
    delay = []

    def __init__(self, cell_type, instance, delay_name, delay):
        self.cell_type = cell_type
        self.instance = instance
        self.delay_name = delay_name
        self.delay = delay
