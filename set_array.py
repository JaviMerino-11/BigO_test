from search_elements.common_data_structures import *
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Different options for data structures')

    parser.add_argument('--structure', '-st', type=str, required=True, help='Choose between list, set or dict')
    parser.add_argument('--limit', '-l', type=int, required=True, help='The numerical extension you want to study')

    return parser.parse_args()


def main():
    args = parse_args()

    if args.structure == 'list':
        search_elem_list(args.limit)
    elif args.structure == 'dict':
        search_elem_dicc(args.limit)
    elif args.structure == 'set':
        search_elem_set(args.limit)
    else:
        print('Choose a valid data structure: list, set or dict')


if __name__ == '__main__':
    main()
