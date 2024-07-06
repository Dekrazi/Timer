import tkinter as tk
from pygame import mixer
from datetime import datetime

timer_running = False

def start_timer():
    global timer_running
    timer_running = True
    input_value = slider.get() * 60  # Convert minutes to seconds
    update_timer(input_value)

def show_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, show_time)

def update_timer(seconds):
    global timer_running
    if seconds >= 0 and timer_running:
        minutes, remaining_seconds = divmod(seconds, 60)
        label.config(text=f"{minutes}:{remaining_seconds:02d}")
        if seconds > 0:
            window.after(1000, update_timer, seconds - 1)
        else:
            label.config(text="Timer completed!")
            timer_running = False
            play_sound()
            slider.set(1)
    else:
        if timer_running:
            label.config(text="Timer completed!")
            timer_running = False
            play_sound()
            slider.set(1)
        else:
            label.config(text="Timer stopped")

def stop_timer():
    global timer_running
    timer_running = False
    label.config(text="Timer stopped")

def add_minutes(value):
    slider.set(value)

def play_sound():
    mixer.init()
    mixer.music.load("super.mp3")
    mixer.music.play()

# Initialize main window
window = tk.Tk()
window.geometry("600x600")
window.title("Timer Application")

# Configure grid layout
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)

# Timer label
label = tk.Label(window, text="", height=1, font=("Helvetica", 30))
label.grid(row=0, column=1, columnspan=2, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

# Time display label
time_label = tk.Label(window, text="", height=1, font=("Helvetica", 16))
time_label.grid(row=1, column=1, columnspan=2, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

# Slider for setting time (1-60 minutes)
slider = tk.Scale(window, from_=1, to=60, orient=tk.HORIZONTAL, length=400,
                sliderlength=20, width=15, 
                highlightthickness=0, bd=0, font=("Helvetica", 12))
slider.grid(row=2, column=1, columnspan=2, pady=20, padx=20, sticky=tk.W + tk.E + tk.N + tk.S)

# Start and Stop buttons
btn_start = tk.Button(window, text="Start", command=start_timer, font=("Helvetica", 12), bg='gray', fg='white')
btn_start.grid(row=3, column=1, pady=10, padx=5, sticky=tk.W + tk.E + tk.N + tk.S)

btn_stop = tk.Button(window, text="Stop", command=stop_timer, font=("Helvetica", 12), bg='gray', fg='white')
btn_stop.grid(row=3, column=2, pady=10, padx=5, sticky=tk.W + tk.E + tk.N + tk.S)

# Time increment buttons frame
increment_frame = tk.Frame(window)
increment_frame.grid(row=4, column=1, columnspan=2, pady=10)

btn_five = tk.Button(increment_frame, text="5 minutes", command=lambda: add_minutes(5), width=12, font=("Helvetica", 12), bg='lightgray', fg='black')
btn_five.grid(row=0, column=0, padx=5)

btn_ten = tk.Button(increment_frame, text="10 minutes", command=lambda: add_minutes(10), width=12, font=("Helvetica", 12), bg='lightgray', fg='black')
btn_ten.grid(row=0, column=1, padx=5)

btn_fifteen = tk.Button(increment_frame, text="15 minutes", command=lambda: add_minutes(15), width=12, font=("Helvetica", 12), bg='lightgray', fg='black')
btn_fifteen.grid(row=0, column=2, padx=5)

# Display current time
show_time()

# Run the application
window.mainloop()
