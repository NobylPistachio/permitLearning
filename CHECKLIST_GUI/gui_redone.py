import tkinter as tk
from tkinter import messagebox

#Master window
class ChecklistGUI():
    def __init__(self, master, sections:list) -> None:
        self.master = master
        self.sections = sections
        #create fields
        self.create_fields()
        self.create_checklist()

        self.create_reset_button()


    def create_fields(self):
        permit_label = tk.Label(self.master, text="Permit #:")
        permit_label.grid(row=0, column=0, sticky="e")
        self.permit_entry = tk.Entry(self.master, width=60)
        self.permit_entry.grid(row=0, column=1, padx=5, sticky="w", columnspan=3)

        address_label = tk.Label(self.master, text="Address:")
        address_label.grid(row=1, column=0, sticky="e")
        self.address_entry = tk.Entry(self.master, width=60)
        self.address_entry.grid(row=1, column=1, padx=5, sticky="w",columnspan=3)

        parcel_label = tk.Label(self.master, text="Parcel #:")
        parcel_label.grid(row=2, column=0, sticky="e")
        self.parcel_entry = tk.Entry(self.master, width=60)
        self.parcel_entry.grid(row=2, column=1, padx=5, sticky="w",columnspan=3)

    def create_checklist(self):
        #get number of checkboxes
            #if I have a load state I want to override this vvv
        self.checklist_states = [False] * len(self.sections)
        self.checkboxes = []
        self.notes_section = []

        #setting up each checkbox, section_label, and note section
        for i, section in enumerate(self.sections):
                #checkbox
            checkbox_var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.master, variable=checkbox_var, command=lambda idx=i: self.toggle_checklist_item(idx))
            self.checkboxes.append(checkbox)
            checkbox.grid(row=i+3, column=0, sticky="e")
            checkbox_var.set(self.checklist_states[i])
            checkbox.checkbox_var = checkbox_var
                #section_label
            section_label = tk.Label(self.master, text=section, wraplength=250)
            section_label.grid(row=i+3, column=1, sticky="w")
                #note_section
            note_section = tk.Entry(self.master, width=30)
                #to be able to interact with the notes section I need to keep it somewhere, that will be the self.notes_section
            self.notes_section.append(note_section)
            note_section.grid(row=i+3, column=2, padx=5, sticky="w")
            


    def toggle_checklist_item(self, index):
        "This will keep track of the var or not maybe this is dumb"
        
        #get which checkbox it is and reverse it
        self.checklist_states[index] = not self.checklist_states[index]
        #

    def reset_fields(self):

            #checkboxes reset works only once
        confirmation = messagebox.askyesno("Reset Confirmation", "Are you sure you want to reset all fields and checklist?")
        if confirmation:
            self.permit_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.parcel_entry.delete(0, tk.END)
            for entry in self.notes_section:
                entry.delete(0, tk.END)
            self.checklist_states = [False] * len(self.sections)
            for num,each in enumerate(self.checkboxes):
                each.checkbox_var.set(self.checklist_states[num])
            # self.update_checklist()
            # self.save_state()  # Save the checklist state

    def create_reset_button(self):
        reset_button = tk.Button(self.master, text="Reset", command=self.reset_fields)
        reset_button.grid(row=len(self.sections) + 3, column=0, columnspan=4, pady=10)

#Settings
title = ""
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
checklist = BR_RMR_CHECKLIST

if __name__ == "__main__":
    root = tk.Tk()
    root.title(title)
    gui = ChecklistGUI(root,checklist)

    #to close the window
    # root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()