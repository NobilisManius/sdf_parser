from numpy import NaN
import re

class Parameter():
    min = NaN
    typical = NaN
    max = NaN

    def __init__(self, line):
        line = re.sub('["| ]', '', line)
        self.min, self.typical, self.max = line.split(':')
