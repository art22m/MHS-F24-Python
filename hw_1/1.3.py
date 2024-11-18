import sys


def get_stats(content):
    lines = content.splitlines()
    words = content.split()
    return len(lines), len(words), len(content.encode())


def wc_command():
    args = sys.argv[1:]
    total_lines, total_words, total_bytes = 0, 0, 0

    if not args:
        file_content = sys.stdin.read()
        total_lines, total_words, total_bytes = get_stats(file_content)
        print(f"\t{total_lines}\t{total_words}\t{total_bytes}")
        return

    for filename in args:
        try:
            with open(filename, "r") as file:
                content = file.read()
        except Exception as e:
            print(f"failed to open file {filename}: {e}")

        curr_lines, curr_words, curr_bytes = get_stats(content)

        total_lines += curr_lines
        total_words += curr_words
        total_bytes += curr_bytes

        print(f"\t{curr_lines}\t{curr_words}\t{curr_bytes}\t{filename}")

    if len(args) > 1:
        print(f"\t{total_lines}\t{total_words}\t{total_bytes}\ttotal")


if __name__ == "__main__":
    wc_command()
