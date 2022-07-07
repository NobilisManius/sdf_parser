def parse(file_name):
    file = open(file_name, mode="rt")
    temp_list = []
    for line in file:
        temp_list.append(line)
    return temp_list


def define_description(parsed_file):
    temp = []

    for line in parsed_file:
        if "(CELL" in line:
            break
        else:
            temp.append(line)

    return tuple(temp)


def slice_cells(parsed_file):
    pass


def parse_cell(sliced_cells):
    pass
