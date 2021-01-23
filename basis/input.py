import sys

read = sys.stdin.readline()
# 1行読む


def input():
    return int(read())
# 1行読む(int)


def line_input():
    return list(map(int, read()))
# 空白区切りでintを読む


def s_input(n):
    return [input() for _ in range(n)]
# n行のintを読む


def m_input(n):
    return [line_input() for i in range(n)]
# n行の空白区切りのintを
