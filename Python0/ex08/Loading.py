#!/usr/bin/env python3.10

import os
import time


def ft_tqdm(lst: range) -> None:
    """
    This functions takes as argument an obj type range.
    We first calculate the width of the terminal:

        os.get_terminal_size() returns an object with 2 attributes:
            .columns)  # largeur du terminal en caractères
            .lines)    # hauteur du terminal en lignes
    total is the length of the list

    in the for loop we iterate in enumerate(lst, 1), which
    will provid a pair : index - elmt in list beginning by 1

    res is the current percentage
    filled is the number already filled in the bar

    bar you will have = and spaces (what it remains)

    os.write accepte only bytes we need to convert it.
    \r : text delete the previous line --> come back to the
    beginning of the line
    """
    termWidth = os.get_terminal_size().columns
    barWidth = termWidth - 40
    total = len(lst)
    for i, item in enumerate(lst, 1):
        res = int((i / total) * 100)
        filled = int(barWidth * i / total)
        bar = "=" * filled + ">" + " " * (barWidth - filled)
        # os.write(1,f"{res}".encode())
        os.write(1, f"\r{res:3d}%|[{bar}]| {i}/{total}".encode())
        yield item
    print()


def main():
    for x in ft_tqdm(range(10)):
        time.sleep(2)


if (__name__ == "__main__"):
    main()
