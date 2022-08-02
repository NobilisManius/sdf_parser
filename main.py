from funcs import *
from description import *

if __name__ == "__main__":

    parsed = parse("lib_sample.sdf")

    descr_tuple = define_description(parsed)


    descr = Description()


    descr.define_descr(descr_tuple)
    
    cells_arr = slice_cells(parse("lib_sample.sdf"))

    test1 = parse_cell(cells_arr)

    print('end')