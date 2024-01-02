import tkinter as tk
from pygame import mixer

def start_timer():
    global timer_running
    timer_running = True
    input_value = int(input_box.get()) * 60  # Convert minutes to seconds
    update_timer(input_value)

def update_timer(seconds):
    global timer_running
    if seconds >= 0 and timer_running:
        minutes, remaining_seconds = divmod(seconds, 60)
        label.config(text=f"Time left: {minutes} minutes {remaining_seconds} seconds")
        if seconds > 0:
            window.after(1000, update_timer, seconds - 1)  
        else:
            label.config(text="Timer completed!")
            timer_running = False
            play_sound()
            input_box.delete(0, tk.END)
    else:
        if timer_running:
            label.config(text="Timer completed!")
            timer_running = False
            play_sound()
            input_box.delete(0, tk.END)
        else:
            label.config(text="Timer stopped")

def stop_timer():
    global timer_running
    timer_running = False
    label.config(text="Timer stopped")
    input_box.delete(0, tk.END) # clear the input box

def add_minutes(value):
    input_box.delete(0, tk.END)
    input_box.insert(tk.END, value)

def play_sound():
    mixer.init()
    mixer.music.load("super.mp3")
    mixer.music.play()


window = tk.Tk()
window.geometry("600x600")

timer_running = False  # Flag to control the timer

label = tk.Label(text="Timer", master=window, height=1)
label.grid(row=0, column=7, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

input_box = tk.Entry()
input_box.grid(row=1, column=7)

btn_start = tk.Button(master=window, text="Start", command=start_timer)
btn_start.grid(row=1, column=8, pady=10)

btn_stop = tk.Button(master=window, text="Stop", command=stop_timer)
btn_stop.grid(row=1, column=9, pady=10)

btn_five = tk.Button(master=window, text="5 minutes", command=lambda: add_minutes(5), width=12)
btn_five.grid(row=3, column=6, pady=10)

btn_ten = tk.Button(master=window, text="10 minutes", command=lambda: add_minutes(10), width=12)
btn_ten.grid(row=3, column=7, pady=10)

btn_fifteen = tk.Button(master=window, text="15 minutes", command=lambda: add_minutes(15), width=12)
btn_fifteen.grid(row=3, column=8, pady=10)

window.mainloop()
