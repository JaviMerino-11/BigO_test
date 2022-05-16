from search_elements.List import Lista
from search_elements.Dict import Dict
from search_elements.Set import Set
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Different options for data structures')

    parser.add_argument('--structure', '-st', type=str, required=True, help='Choose between list, set or dict')
    parser.add_argument('--limit', '-l', type=int, required=True, help='The numerical extension you want to study')

    return parser.parse_args()


def main():
    args = parse_args()

    if args.structure == 'list':
        lista = Lista(structure_type=args.structure, numerical_limit=args.limit)
        lista.search_element_list()
    elif args.structure == 'dict':
        dict = Dict(structure_type=args.structure, numerical_limit=args.limit)
        dict.search_element_dict()
    elif args.structure == 'set':
        set = Set(structure_type=args.structure, numerical_limit=args.limit)
        set.search_element_set()
    else:
        print('Choose a valid data structure: list, set or dict')


if __name__ == '__main__':
    main()
