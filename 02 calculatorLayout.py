import tkinter as tk

root = tk.Tk()
root.title("Calculator Layout")
# ==============
# Text widget
text = tk.Text(root)
text.configure(background="light grey", foreground="dark red", width=20, height=4, borderwidth=5)
text.insert(tk.END, "This is a text widget demo!")
text.grid(column=0, row=0, columnspan=3)

# Button widgets
# tk.Button(root, text='*', width=6).grid(row=1, column=0)
# tk.Button(root, text='^', width=6).grid(row=1, column=1)
# tk.Button(root, text='#', width=6).grid(row=1, column=2)
# tk.Button(root, text='<', width=6).grid(row=2, column=0)
# tk.Button(root, text='OK', width=6).grid(row=2, column=1)
# tk.Button(root, text='>', width=6).grid(row=2, column=2)
# tk.Button(root, text='+', width=6).grid(row=3, column=0)
# tk.Button(root, text='v', width=6).grid(row=3, column=1)
# tk.Button(root, text='-', width=6).grid(row=3, column=2)
# tk.Button(root, text='1', width=6).grid(row=4, column=0)
# tk.Button(root, text='2', width=6).grid(row=4, column=1)
# tk.Button(root, text='3', width=6).grid(row=4, column=2)
# tk.Button(root, text='4', width=6).grid(row=5, column=0)
# tk.Button(root, text='5', width=6).grid(row=5, column=1)
# tk.Button(root, text='6', width=6).grid(row=5, column=2)
# tk.Button(root, text='7', width=6).grid(row=6, column=0)
# tk.Button(root, text='8', width=6).grid(row=6, column=1)
# tk.Button(root, text='9', width=6).grid(row=6, column=2)
# ==============
# rewrite Button widgets
letters = [['*', '^', '#'],
           ['<', 'OK', '>'],
           ['+', 'v', '-'],
           ['1', '2', '3'],
           ['4', '5', '6'],
           ['7', '8', '9']
           ]
rows = [1, 2, 3, 4, 5, 6]
columns = [0, 1, 2]

for row in rows:
    for column in columns:
        tk.Button(root, text=letters[row-1][column], width=6).grid(row=row, column=column)
# ===============

root.mainloop()
