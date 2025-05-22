import math
from tkinter import *

# ------------------------------CONSTANTS-------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# -------------------------------Time reset-----------------------#

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")

# -------------------------------TIMER MECHANISM-------------------#
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# -------------------------------COUNTER MECHANISM------------------#
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)



# --------------------------------UI SETUP--------------------------#

window = Tk()
window.title("pomodro")
window.config(padx=80, pady=40, bg=YELLOW)
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 75, "bold"))
title_label.grid(row=0, column=1)

canvas = Canvas(width=356, height=405, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.PNG")
canvas.create_image(176, 199, image=tomato_image)
timer_text = canvas.create_text(176, 230, text="00:00", fill="white", font=(FONT_NAME, 45, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"), highlightthickness=0)
check_mark.grid(row=3, column=1)
window.mainloop()
