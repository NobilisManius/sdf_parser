from cell import Cell
import copy

def parse(file_name):
    """Parse the file into list of lines."""
    file = open(file_name, mode="rt")
    temp_list = []
    for line in file:
        temp_list.append(line)
    return temp_list


def define_description(parsed_file):
    """Find the description of delayfile and return it as tuple."""
    temp = []

    for line in parsed_file:
        if "(CELL" in line:
            break
        elif "(DELAYFILE" in line:
            continue
        else:
            temp.append(line.translate({ord(i): None for i in ')'}))

    return tuple(temp)


def slice_cells(parsed_file):
    """Slice parsed file into cells and return them as nested list."""
    indexes = []
    temp = []
    for index, line in enumerate(parsed_file):
        if line == ' (CELL\n' or line == ' )\n':
            indexes.append(index)

    for i in range(0, len(indexes), 2):
        temp.append(parsed_file[indexes[i]:indexes[i + 1]])

    return temp

def parse_cell(sliced_cells):
    """Parse a cells and return them as list of class objects."""
    meta_data = []
    data = []
    cells = []
    indexes = []
    data_start = 0
    data_end = 0

    for i, cell in enumerate(sliced_cells):
        for j, line in enumerate(cell):
            if "(DELAY" in line:
                data_start = j
                break
            elif "(CELL\n" not in line:
                meta_data.append(line.translate({ord(i): None for i in ')'}))

        data_end = len(cell)
        data = (cell[data_start:data_end])
        meta_data.append(copy.deepcopy(data[1]))
        del data[0:1]
        cell_obj = Cell(meta_data, data)
        cells.append(cell_obj)
        data.clear()
        meta_data.clear()
    return cells


    pass
