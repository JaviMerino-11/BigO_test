from search_elements.list_structure import List_Structure
from search_elements.dict_structure import Dict_Structure
from search_elements.set_structure import Set_Structure
from search_elements.tuple_structure import Tuple_Structure

import argparse
import sys

STRUCTURE_TYPE_LIST = 'list'
STRUCTURE_TYPE_SET = 'set'
STRUCTURE_TYPE_DICT = 'dict'
STRUCTURE_TYPE_TUPLE = 'tuple'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Different options for data structures')

    parser.add_argument('--structure', '-st', type=str, required=True, help='Choose between list, set, tuple or dict')
    parser.add_argument('--limit', '-l', type=int, required=True, help='The numerical extension you want to study')

    return parser.parse_args()


def main():
    args = parse_args()
    structure_type = args.structure
    numerical_limit = args.limit

    if numerical_limit >= 0:
        if structure_type == STRUCTURE_TYPE_LIST:
            list_structure = List_Structure(structure_type=structure_type, numerical_limit=numerical_limit)
            list_structure.search_element_list()
        elif structure_type == STRUCTURE_TYPE_DICT:
            dict_structure = Dict_Structure(structure_type=structure_type, numerical_limit=numerical_limit)
            dict_structure.search_element_dict()
        elif structure_type == STRUCTURE_TYPE_SET:
            set_structure = Set_Structure(structure_type=structure_type, numerical_limit=numerical_limit)
            set_structure.search_element_set()
        elif structure_type == STRUCTURE_TYPE_TUPLE:
            tuple_structure = Tuple_Structure(structure_type=structure_type, numerical_limit=numerical_limit)
            tuple_structure.search_element_tuple()
        else:
            print('Choose a valid data structure: list, set, tuple or dict')
            sys.exit(-1)
    else:
        print('Introduce a numerical limit greater than 0')
        sys.exit(-1)


if __name__ == '__main__':
    main()
