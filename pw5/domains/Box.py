import curses
from curses.textpad import Textbox, rectangle

def makebox(stdscr, content, height, width, begin_x, begin_y):
    stdscr.addstr(begin_x, begin_y, content)
    win = curses.newwin(height, width, begin_x, begin_y + 25)
    box = Textbox(win)
    rectangle(stdscr, begin_x - 1, begin_y + 25 - 1, begin_x + height, begin_y + width + 25)
    return box
  