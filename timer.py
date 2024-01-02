import tkinter as tk

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
            window.after(1000, update_timer, seconds - 1)  # Update every 1000 milliseconds (1 second)
        else:
            label.config(text="Timer completed!")
            timer_running = False
    else:
        if timer_running:
            label.config(text="Timer completed!")
            timer_running = False
        else:
            label.config(text="Timer stopped")


def stop_timer():
    global timer_running
    timer_running = False
    label.config(text="Timer stopped")
    input_box.delete(0, tk.END)

window = tk.Tk()

timer_running = False  # Flag to control the timer

label = tk.Label(text="Timer", master=window, height=1)
label.grid(row=0, column=0, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

input_box = tk.Entry()
input_box.grid(row=1, column=0)

btn_start = tk.Button(master=window, text="Start", command=start_timer)
btn_start.grid(row=2, column=5, pady=10)

btn_stop = tk.Button(master=window, text="Stop", command=stop_timer)
btn_stop.grid(row=2, column=6, pady=10)

window.mainloop()
