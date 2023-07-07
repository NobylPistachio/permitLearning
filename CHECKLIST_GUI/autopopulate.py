import gui_redone
from gui_redone import main as boi
from gui_redone import checklist
import tkinter as tk
from tkinter import ttk

title = "testing"





def autopopulate(self):
    ...

gui_redone.ChecklistGUI.autopopulate = autopopulate

def create_custom_button(self,button_text:str, button_command, button_row:int, button_column:int, master):
    button = tk.Button(master, text=button_text, command=button_command)
    button.grid(row=button_row, column=button_column, columnspan=1, pady=10, sticky="")
    return button

gui_redone.ChecklistGUI.create_custom_button = create_custom_button

def main():
    root = tk.Tk()
    root.title("Pinellas County Permit Utility")
    
    notebook = ttk.Notebook(root)
    notebook.pack()

    tab1 = tk.Frame(notebook)
    # tab2 = tk.Frame(notebook)

    gui_redone.ChecklistGUI.create_custom_button(,button_text = "Autopopulate", button_command = autopopulate, button_row = 2, button_column = 4, master = tab1)
    
    notebook.add(tab1, text=title)
    # notebook.add(tab2, text="Tab 2")

    gui = gui_redone.ChecklistGUI(tab1,checklist,title)

    #to close the window
    # root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

main()