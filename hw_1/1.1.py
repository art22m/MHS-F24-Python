import sys


def number_lines(lines):
    num = 0
    for line in lines:
        if len(line.strip()) == 0:
            print(f"\t{line}", end='')
            continue
        num += 1
        print(f"\t{num}\t{line}", end='')


def main():
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], "r") as file:
                number_lines(file)
        except Exception as e:
            print(f"failed to open file: {e}")
    else:
        number_lines(sys.stdin)


if __name__ == "__main__":
    main()
