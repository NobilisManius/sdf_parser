"""
Delay file contains several parameters, such as divider and voltage.
Since these parameters are constant, I decided to make a standalone class.
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

    def Description(self, data_line):
        self.sdfversion, self.design, self.date, self.vendor, self.program, self.version, self.divider, self.voltage, \
        self.process, self.temperature, self.timescale = data_line

        self.sdfversion = self.sdfversion.split()[1]
        self.design = self.design.split()[1]
        self.date = self.date.split(maxsplit=1)[1]
        self.vendor = self.vendor.split()[1]
        self.program = self.program.split()[1]
        self.version = self.version.split()[1]
        self.divider = self.divider.split()[1]
        self.voltage = self.voltage.split()[1]
        self.process = self.process.split()[1]
        self.temperature = self.temperature.split()[1]
        self.timescale = self.timescale.split()[1]
