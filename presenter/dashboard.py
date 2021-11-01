import sys
sys.path.append("..")

from model.book_entry import BookEntry
import asyncio
import book_ticker
from view import dashboard


loop = asyncio.get_event_loop()
def update_book_callback(update):
    book_entry = BookEntry(update)
    if book_entry.is_valid:
        dashboard.update_book(book_entry)

async def init():

    dashboard.start()

    book_ticker.spot_websocket_client.start()
    book_ticker.callback = update_book_callback
    book_ticker.subscribe()
    
try:
    asyncio.ensure_future(init())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
    curses.nocbreak()
    curses.echo()
    curses.endwin()

