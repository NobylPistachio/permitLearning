import tkinter as tk
from tkinter import messagebox
import pickle
import logging

logging.basicConfig(filename='checklist_gui.log',encoding='utf-8', level=logging.DEBUG)

def logger(func):
    def wrapper():
        ...

class ChecklistGUI:
    def __init__(self, master, sections:list):
        self.master = master
        self.sections = sections
        self.checklist_states = [False] * len(self.sections)
        
        self.create_fields()
        self.create_checklist()
        #self.create_reset_button()

        self.load_state()  # Load the state from a previous session

        print(self.checklist_states)

    def create_fields(self):
        permit_label = tk.Label(self.master, text="Permit #:")
        permit_label.grid(row=0, column=0, sticky="e")
        self.permit_entry = tk.Entry(self.master)
        self.permit_entry.grid(row=0, column=1)

        address_label = tk.Label(self.master, text="Address:")
        address_label.grid(row=1, column=0, sticky="e")
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=1, column=1)

        parcel_label = tk.Label(self.master, text="Parcel #:")
        parcel_label.grid(row=2, column=0, sticky="e")
        self.parcel_entry = tk.Entry(self.master)
        self.parcel_entry.grid(row=2, column=1)

    def create_checklist(self):
        for i, section in enumerate(self.sections):
            checkbox_var = tk.BooleanVar()
            checkbox_var.set(self.checklist_states[i])
            checkbox = tk.Checkbutton(self.master, variable=checkbox_var, command=lambda idx=i: self.toggle_checklist_item(idx))
            checkbox.grid(row=i + 3, column=0, sticky="w")

            label = tk.Label(self.master, text=section)
            label.grid(row=i + 3, column=1, sticky="w")

    def create_reset_button(self):
        
        self.checklist_states = [False] * len(self.sections)

    def toggle_checklist_item(self, index):
        self.checklist_states[index] = not self.checklist_states[index]
        self.update_checklist()
        # self.save_state() # Save the checklist state

    def update_checklist(self):
        all_complete = all(self.checklist_states)
        if all_complete:
            messagebox.showinfo(f"Checklist Complete", "Congratulations! Checklist is complete.")

    def save_state(self):
        state = {
            'checklist_states': self.checklist_states,
            'permit_number': self.permit_entry.get(),
            'address': self.address_entry.get(),
            'parcel_number': self.parcel_entry.get()
        }
        with open('checklist_state.pkl', 'wb') as f:
            pickle.dump(state, f)

    def load_state(self):
            try:
                with open('checklist_state.pkl', 'rb') as f:
                    state = pickle.load(f)
                    self.checklist_states = state['checklist_states']
                    self.permit_entry.insert(0, state['permit_number'])
                    self.address_entry.insert(0, state['address'])
                    self.parcel_entry.insert(0, state['parcel_number'])
            except FileNotFoundError:
                pass


BR_RMR_CHECKLIST:list = ["Check Jurisdiction",
                    "Check for duplicate permits",
                    "Check for Violations",
                    "Check Licensed Professionals Attached",
                    "Check if Private Provider",
                    "Check for open permits",
                    "Check submitted documents",
                    "Check NOC requirement",
                    'Enter or verify "Standard Description" and use established naming convention',
                    "Deem Complete"
                    ]

if __name__ == "__main__":
    root = tk.Tk()
    root.title("BR-RMR Checklist")
    gui = ChecklistGUI(root,BR_RMR_CHECKLIST)

    def on_closing():
        gui.save_state()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()