import tkinter as tk
root = tk.Tk()

# ==============
# Create a label
label = tk.Label(root)
label.configure(text="A Label")
label.pack()

# Add a button
button = tk.Button(root)
button.configure(text="A Button")
button.pack()
# ==============

root.mainloop()
