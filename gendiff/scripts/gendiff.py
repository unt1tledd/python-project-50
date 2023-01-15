import argparse
from gendiff.generate_diff import generate_diff


def parse():
    parser = argparse.ArgumentParser(
            description = 'Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format')
    return parser.parse_args()


def main():
    args = parse()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()


