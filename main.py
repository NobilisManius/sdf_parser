from funcs import parse
from funcs import define_description
from funcs import slice_cells
from funcs import parse_cell
import description

if __name__ == "__main__":
    # test = description.Description()
    # test.Description(define_description(parse("b11.sdf")))
    test = slice_cells(parse("b11.sdf"))
    test1 = parse_cell(test)
    pass
