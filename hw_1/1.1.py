import sys


def number_lines(input_stream):
    for line_number, line in enumerate(input_stream, start=1):
        print(f"{line_number}\t{line}", end='')


def main():
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1]) as file:
                number_lines(file)
        except Exception as e:
            print(f"failed to open file: {e}")
    else:
        number_lines(sys.stdin)


if __name__ == "__main__":
    main()
