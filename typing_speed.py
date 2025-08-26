import curses #This project uses curses library.
from curses import wrapper #Wrapper is used for running the app in a wrapper.
import time
import random

def start_screen(stdscr):
    stdscr.clear() #For clearing the screen
    stdscr.addstr("Welcome to Speed typing test!\n") #For adding string to the screen.
    stdscr.addstr("Press any key to begin...")
    stdscr.refresh()
    stdscr.getkey() #Getting a key from the user.

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(0, 0, target, curses.color_pair(3))  # target text
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)
    
def get_text(): #Getting random strings to the app.
    with open("test_texts.txt", "r") as f:
        lines = f.readlines()
        f.close()
    return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = get_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True) #Setting the getkey() function for not making delay.
    curses.curs_set(0) #Avoiding the blinking of the cursor.
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5) #Calculating wpm.

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text: #Converting the list to a string for comparing.
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # ESC key
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"): #Checking and handling the backspace key.
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # correct chars
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # incorrect chars
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # base text

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(3, 0, "Completed! Press any key to exit...")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)
