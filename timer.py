import tkinter as tk
from tkinter import ttk
window = tk.Tk()
label = tk.Label(text="Timer")
label.pack()

# Add a progress bar
# p = ttk.Progressbar(parent, orient=HORIZONTAL, length=200, mode='determinate')

button_start = tk.Button(text="Start")
button_start.pack()
button_stop = tk.Button(text="Stop")
button_stop.pack()

window.mainloop()
