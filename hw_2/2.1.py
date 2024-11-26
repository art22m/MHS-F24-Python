from art22m_latex import latex_generator


def main():
    data = [
        ["Column1", "Column2", "Column3"],
        ["1", "Test1", 100],
        ["2", "Test2", 200],
        ["3", "Test3", 300]
    ]

    table = latex_generator.generate_table(data)

    with open("artifacts/out2.1.tex", "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage[utf8]{inputenc}\n")
        f.write("\\usepackage{graphicx}\n")
        f.write("\\begin{document}\n")
        f.write(table)
        f.write("\n\\end{document}")


if __name__ == "__main__":
    main()
