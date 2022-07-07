"""
delay file contains several parameters, such as divider and voltage.
Since these parameters are constant, I decided to make a class.
"""


class Description:
    sdfversion = ''
    design = ''
    date = ''
    vendor = ''
    program = ''
    version = ''
    divider = ''
    voltage = ''
    process = ''
    temperature = ''
    timescale = ''

    def __init__(self):
        pass

    def Description(self, sdfversion, design, date, vendor, program, version, divider, voltage, process, temperature, timescale):
        self.sdfversion = sdfversion
        self.design = design
        self.date = date
        self.vendor = vendor
        self.program = program
        self.version = version
        self.divider = divider
        self.voltage = voltage
        self.process = process
        self.temperature = temperature
        self.timescale = timescale
