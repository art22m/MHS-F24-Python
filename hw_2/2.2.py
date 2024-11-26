import art22m_latex


def main():
    data = [
        ["Column1", "Column2", "Column3"],
        ["1", "Test1", 100],
        ["2", "Test2", 200],
        ["3", "Test3", 300]
    ]

    table = art22m_latex.generate_table(data)
    image = art22m_latex.generate_image("./sample_image.jpg", "test-image", "fig:test-image")

    with open("artifacts/out2.2.tex", "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage[utf8]{inputenc}\n")
        f.write("\\usepackage{graphicx}\n")
        f.write("\\begin{document}\n")
        f.write(image)
        f.write(table)
        f.write("\n\\end{document}")


if __name__ == "__main__":
    main()
