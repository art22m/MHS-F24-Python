import sys


def process_file(filename, n, print_file_name):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if print_file_name:
                print(f"==> {filename} <==")
            print(''.join(lines[-n:]), end='')
    except Exception as e:
        print(f"failed to open file {filename}: {e}")


def main():
    args = sys.argv[1:]
    if args:
        for i, filename in enumerate(args):
            if i > 0:
                print()
            process_file(filename, 10, len(args) > 1)
    else:
        input_lines = sys.stdin.readlines()
        tail_lines = input_lines[-17:]
        print(''.join(tail_lines), end='')


if __name__ == "__main__":
    main()
