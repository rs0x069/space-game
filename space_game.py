import asyncio
import curses
import time


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)


# def draw(canvas):
#     while True:
#         row, column = (5, 20)
#         canvas.border()
#
#         canvas.addstr(row, column, '*', curses.A_DIM)
#         canvas.refresh()
#         time.sleep(2)
#
#         canvas.addstr(row, column, '*', curses.A_NORMAL)
#         canvas.refresh()
#         time.sleep(0.3)
#
#         canvas.addstr(row, column, '*', curses.A_BOLD)
#         canvas.refresh()
#         time.sleep(0.5)
#
#         canvas.addstr(row, column, '*', curses.A_NORMAL)
#         canvas.refresh()
#         time.sleep(0.3)


def draw(canvas):
    row, column = (5, 20)
    canvas.border()

    coroutine = blink(canvas, row, column)

    coroutines = [
        blink(canvas, row, 5),
        blink(canvas, row, 8),
        blink(canvas, row, 11),
        blink(canvas, row, 14),
        blink(canvas, row, 17),
    ]

    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                break
        canvas.refresh()
        time.sleep(1)

        # coroutine.send(None)
        # canvas.refresh()
        # time.sleep(1)


def main():
    curses.update_lines_cols()
    curses.wrapper(draw)
    curses.curs_set(False)


if __name__ == '__main__':
    main()
