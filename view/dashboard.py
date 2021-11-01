import curses
from config.general import TRAIDING_SYMBOLS
from config.style import PRICE_FORMAT, QTY_FORMAT, PRIMARY_COLOR_PAIR, SECONDARY_COLOR_PAIR, ACCENT_COLOR_PAIR, POSITIVE_COLOR_PAIR, NEGATIVE_COLOR_PAIR, COLUMN_COLOR_PAIR, ROW_COLOR_PAIR
from model.book_entry import BookEntry

#TODO Abstract the view to facilitate have more that feed per console : )

C = 3
C1 = C + 10
C2 = C1 + 25
C3 = C2 + 25
C4 = C3 + 25

def get_l(symbol):
    return 3+TRAIDING_SYMBOLS.index(symbol)

stdscr = None
def start():
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    # stdscr.keypad(True)

    stdscr.clear()

    stdscr.addstr(1, C1, 'best bid price', COLUMN_COLOR_PAIR)
    stdscr.addstr(1, C2, 'best bid qty', COLUMN_COLOR_PAIR)
    stdscr.addstr(1, C3, 'best ask price', COLUMN_COLOR_PAIR)
    stdscr.addstr(1, C4, 'best ask qty', COLUMN_COLOR_PAIR)

    for symbol in TRAIDING_SYMBOLS:
        l = get_l(symbol)
        stdscr.addstr(l, C, symbol, ROW_COLOR_PAIR)

    stdscr.refresh()


def stop():
    curses.nocbreak()
    # stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def update_book(book_entry):

    l = get_l(book_entry.traiding_symbol)

    stdscr.addstr(l, C1, book_entry.best_bid_price, SECONDARY_COLOR_PAIR)
    stdscr.addstr(l, C2, book_entry.best_bid_qty, ACCENT_COLOR_PAIR)
    stdscr.addstr(l, C3, book_entry.best_ask_price, POSITIVE_COLOR_PAIR)
    stdscr.addstr(l, C4, book_entry.best_ask_qty, NEGATIVE_COLOR_PAIR)
    stdscr.refresh()