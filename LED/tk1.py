import tkinter as tk

def submit_data():
    digital_pin = digital_pin_entry.get()
    time_on = time_on_entry.get()
    time_off = time_off_entry.get()
    print("Digital Pin No:", digital_pin)
    print("Time On:", time_on)
    print("Time Off:", time_off)

root = tk.Tk()
root.title("Welcome to our program")
root.geometry("480x480")

heading_label = tk.Label(root, text="Welcome to my program", font=("Arial", 16, "bold"))
heading_label.pack(pady=10)

# Input boxes
digital_pin_label = tk.Label(root, text="Digital Pin No")
digital_pin_label.pack()
digital_pin_entry = tk.Entry(root)
digital_pin_entry.pack(pady=5)

time_on_label = tk.Label(root, text="Time On")
time_on_label.pack()
time_on_entry = tk.Entry(root)
time_on_entry.pack(pady=5)

time_off_label = tk.Label(root, text="Time Off")
time_off_label.pack()
time_off_entry = tk.Entry(root)
time_off_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.pack(pady=10)

root.mainloop()

