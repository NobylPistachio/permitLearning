import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#---- TO DO --------------------------------
# Button to easy open Accela, and PCPAO
# Add Work description section
#-------------------------------------------
#Master window
class ChecklistGUI():
    def __init__(self, master, sections:list, checklist_title:str="") -> None:
        self.master = master
        self.sections = sections
        self.checklist_title = checklist_title
        #create fields
        self.create_fields()
        self.create_checklist()

        self.create_buttons()

    def create_field(self, label_text, grid_row):
        "This creates a field for notes"
        label = tk.Label(self.master, text=label_text)
        label.grid(row=grid_row, column=0, sticky="e")
        entry = tk.Entry(self.master, width=60)
        entry.grid(row=grid_row, column=1, padx=5, sticky="w", columnspan=3)
        return entry


    def create_fields(self):
        "This function is for creating the top section of the page, for holding basic identifying information of a permit"
        self.permit_entry = self.create_field("Permit #:",grid_row=0)
        self.address_entry = self.create_field("Address:",grid_row=1)
        self.parcel_entry = self.create_field("Parcel #:",grid_row=2)

        self.fields_entry = [self.permit_entry,self.address_entry,self.parcel_entry]


    def create_checklist(self):
        #get number of checkboxes
            #if I have a load state I want to override this vvv
        self.checklist_states = [False] * len(self.sections)
        self.checkboxes = []
        self.notes_section = []

        #setting up each checkbox, section_label, and note section
        for i, section in enumerate(self.sections):

            #checklist settings
            populated_row = i+3

                #checkbox
            checkbox_var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.master, variable=checkbox_var, command=lambda idx=i: self.toggle_checklist_item(idx))
            self.checkboxes.append(checkbox)
            checkbox.grid(row=populated_row, column=0, sticky="e")
            checkbox_var.set(self.checklist_states[i])
            checkbox.checkbox_var = checkbox_var
                #section_label
            section_label = tk.Label(self.master, text=section, wraplength=250)
            section_label.grid(row=populated_row, column=1, sticky="w")
                #note_section
            note_section = tk.Entry(self.master, width=50)
                #to be able to interact with the notes section I need to keep it somewhere, that will be the self.notes_section
            self.notes_section.append(note_section)
            note_section.grid(row=populated_row, column=2, padx=5, sticky="w")


    def toggle_checklist_item(self, index):
        "This will keep track of the var or not maybe this is dumb"
        
        #get which checkbox it is and reverse it
        self.checklist_states[index] = not self.checklist_states[index]
        #


    def reset_fields(self,message:bool=True):
            #checkboxes reset works only once
        confirmation = True
        if message:
            confirmation = messagebox.askyesno("Reset Confirmation", "Are you sure you want to reset all fields and checklist?")
        if confirmation:
            for entry in self.notes_section + self.fields_entry:
                entry.delete(0, tk.END)
            self.checklist_states = [False] * len(self.sections)
            for num,each in enumerate(self.checkboxes):
                each.checkbox_var.set(self.checklist_states[num])
            # self.update_checklist()
            # self.save_state()  # Save the checklist state

    def create_button(self, button_text:str, button_command, button_column:int):
        button = tk.Button(self.master, text=button_text, command=button_command)
        button.grid(row=len(self.sections) + 3, column=button_column, columnspan=1, pady=10, sticky="")
        return button

    def create_buttons(self):
        self.reset_button = self.create_button("Reset",self.reset_fields,0)
        self.save_button = self.create_button("Save",self.save_state,1)
        self.load_button = self.create_button("Load",self.load_state,2)
    
    def save_state(self):

        state = {
            'checklist type': self.checklist_title,
            'fields': [field.get() for field in self.fields_entry],
            'checklist_states': self.checklist_states,
            'notes': [entry.get() for entry in self.notes_section]
        }
        with open('checklist_state.txt', 'w') as f:
            for key, value in state.items():
                f.write(f"{key}: {value}\n")
    
    def load_state(self):
        try:
            with open('checklist_state.txt', 'r') as f:
                state = {}
                for line in f:
                    key, value = line.strip().split(': ')
                    if key == 'checklist type':
                        state[key] = value
                    elif key in ['fields','notes']:
                        state[key] = [elem.strip("[]'") for elem in value.split(", ")]
                    elif key == 'checklist_states':
                        str_to_bool = lambda x: True if x == "True" else False
                        save_states = [str_to_bool(v.strip("[]")) for v in value.split(', ')]
                        state[key] = save_states


            # 'checklist type': self.checklist_title,
            # 'fields': [field for field in self.fields_entry],
            # 'checklist_states': self.checklist_states,
            # 'notes': [entry.get() for entry in self.notes_section]
                self.reset_fields(False)

                self.checklist_title = state["checklist type"]

                self.permit_entry.insert(0, state["fields"][0])
                self.address_entry.insert(0, state["fields"][1])
                self.parcel_entry.insert(0, state["fields"][2])

                self.checklist_states = [box for box in state["checklist_states"]]
                for num,each in enumerate(self.checkboxes):
                    each.checkbox_var.set(self.checklist_states[num])

                for num,entry in enumerate(self.notes_section):
                    entry.insert(0, state["notes"][num])

        except FileNotFoundError:
            self.checklist_states = [False] * len(self.sections)



#Settings
title = "BR-RMR Checklist"
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
    root.title("Pinellas County Permit Utility")
    
    notebook = ttk.Notebook(root)
    notebook.pack()

    tab1 = tk.Frame(notebook)
    # tab2 = tk.Frame(notebook)

    notebook.add(tab1, text=title)
    # notebook.add(tab2, text="Tab 2")

    gui = ChecklistGUI(tab1,checklist,title)

    #to close the window
    # root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()