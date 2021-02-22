#!/usr/bin/env python3

import sys


def read_single_keypress():
    """Waits for a single keypress on stdin.

    This is a silly function to call if you need to do it a lot because it has
    to store stdin's current setup, setup stdin for reading single keystrokes
    then read the single keystroke then revert stdin back after reading the
    keystroke.

    Returns a tuple of characters of the key that was pressed - on Linux,
    pressing keys like up arrow results in a sequence of characters. Returns
    ('\x03',) on KeyboardInterrupt which can happen when a signal gets
    handled.

    """
    import termios, fcntl, sys, os

    fd = sys.stdin.fileno()
    # save old state
    flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
    attrs_save = termios.tcgetattr(fd)
    # make raw - the way to do this comes from the termios(3) man page.
    attrs = list(attrs_save)  # copy the stored version to update
    # iflag
    attrs[0] &= ~(
        termios.IGNBRK
        | termios.BRKINT
        | termios.PARMRK
        | termios.ISTRIP
        | termios.INLCR
        | termios.IGNCR
        | termios.ICRNL
        | termios.IXON
    )
    # oflag
    attrs[1] &= ~termios.OPOST
    # cflag
    attrs[2] &= ~(termios.CSIZE | termios.PARENB)
    attrs[2] |= termios.CS8
    # lflag
    attrs[3] &= ~(
        termios.ECHONL | termios.ECHO | termios.ICANON | termios.ISIG | termios.IEXTEN
    )
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    # turn off non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)
    # read a single keystroke
    ret = []
    try:
        ret.append(sys.stdin.read(1))  # returns a single character
        fcntl.fcntl(fd, fcntl.F_SETFL, flags_save | os.O_NONBLOCK)
        c = sys.stdin.read(1)  # returns a single character
        while len(c) > 0:
            ret.append(c)
            c = sys.stdin.read(1)
    except KeyboardInterrupt:
        ret.append("\x03")
    finally:
        # restore old state
        termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
    return tuple(ret)


def play(board, move):
    if move >= 0 and move < len(board):
        move = "    " + "①②③④⑤⑥⑦⑧⑨⑩"[move]
    else:
        move = ""
    line = " ".join("▲" if i > 0 else "▼" for i in board)
    print(f"\033[32m{line}\033[0m{move}", end="\n")

    if all(i == -1 for i in board):
        return True

    print("\033[2m" + " ".join("₁₂₃₄₅₆₇₈₉₀"[: len(board)]) + "\033[0m")
    return False


print("\033[H\033[2J", end="")  # clear

try:
    size = int(sys.argv[1])
    if size < 2 or size > 10:
        raise ValueError
except (IndexError, ValueError):
    size = 6

board = [1] * size
move = -1
while True:
    if play(board, move):
        print("Gagné")
        break

    key = "".join(read_single_keypress())
    if len(key) != 1:
        continue

    if key in "xXqQ\03\033":  # Echap, ^C, x, q pour quitter
        break

    if key == "R":  # recommencer
        board = [1] * len(board)
        continue

    move = "&é\"'(§è!çà".find(key)
    if move == -1:
        move = "1234567890".find(key)
    if move == -1 or move >= len(board):
        continue
    board = [-v if i != move else v for i, v in enumerate(board)]
