import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

image = Image.open(r"CHECKLIST_GUI/my_image.jpg")
# my_image = ImageTk.PhotoImage(image)

root = tk.Tk()
notebook = ttk.Notebook(root)
notebook.pack()
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
 # Set the compound option to combine text and image
notebook.tab(tab1, compound=tk.LEFT, text="Tab 1", image=image)
root.mainloop()