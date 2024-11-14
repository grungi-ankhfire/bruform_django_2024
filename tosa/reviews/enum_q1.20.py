def sudoku_line(line):
    for i in range(1, 10):
        if i not in line:
            number = i
            break  # Totalement optionel, ça marche sans

    for i, b in enumerate(line):
        if b == -1:
            line[i] = number

    return line

assert sudoku_line([1, 2, 3, 4, 5, -1, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sudoku_line([2, 3, 4, 6, 5, 1, 7, 9, -1]) == [2, 3, 4, 6, 5, 1, 7, 9, 8]