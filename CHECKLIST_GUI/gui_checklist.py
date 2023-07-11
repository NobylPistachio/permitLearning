import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#---- TO DO --------------------------------
# Button to easy open Accela, and PCPAO
# Add Work description section
# Make a tab that can add more tabs
# Upon closing make it so that it will ask to save, make it more like notepad when saving
# debate if you want to use pickle or not
# implement logging into this, use decorators
#-------------------------------------------
# Main class for the GUI
class ChecklistGUI():
    def __init__(self, master, sections:list, checklist_title:str="") -> None:
        # Initialize master, sections, and checklist title
        self.master = master
        self.sections = sections
        self.checklist_title = checklist_title
         # Initialize fields, checklist, and buttons
        self.create_fields()

        # self.create_workdescription()

        self.create_checklist()
        self.create_buttons()
    def create_field(self, label_text, grid_row):
        """Creates a field for notes"""
        label = tk.Label(self.master, text=label_text)
        label.grid(row=grid_row, column=0, sticky="e")
        entry = tk.Entry(self.master, width=60)
        entry.grid(row=grid_row, column=1, padx=5, sticky="w", columnspan=3)
        return entry
    def create_fields(self):
        """Creates the top section of the page, for holding basic identifying information of a permit"""
        self.permit_entry = self.create_field("Permit #:", grid_row=0)
        self.address_entry = self.create_field("Address:", grid_row=1)
        self.parcel_entry = self.create_field("Parcel #:", grid_row=2)
        self.fields_entry = [self.permit_entry, self.address_entry, self.parcel_entry]
    def create_workdescription(self):
        label = tk.Label(self.master, text= "Work Description")
        label.grid(rowspan=2, column=0, columnspan= 1, sticky="e")
        entry = tk.Entry(self.master, width=60)
        entry.grid(column = 1)
        ...
    def create_checklist(self):
        """Creates the checklist"""
        # Initialize checklist states, checkboxes, and notes section
        self.checklist_states = [False] * len(self.sections)
        self.checkboxes = []
        self.notes_section = []
         # Setting up each checkbox, section_label, and note section
        for i, section in enumerate(self.sections):
            rows,columns = self.master.grid_size()
            populated_row = i + rows
             # Checkbox settings
            checkbox_var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.master, variable=checkbox_var, command=lambda idx=i: self.toggle_checklist_item(idx))
            self.checkboxes.append(checkbox)
            checkbox.grid(row=populated_row, column=0, sticky="e")
            checkbox_var.set(self.checklist_states[i])
            checkbox.checkbox_var = checkbox_var
             # Section label settings
            section_label = tk.Label(self.master, text=section, wraplength=250)
            section_label.grid(row=populated_row, column=1, sticky="w")
             # Note section settings
            note_section = tk.Entry(self.master, width=50)
                #to be able to interact with the notes section I need to keep it somewhere, that will be the self.notes_section
            self.notes_section.append(note_section)
            note_section.grid(row=populated_row, column=2, padx=5, sticky="w")
    def toggle_checklist_item(self, index):
        """Toggles the checklist item at the given index"""
        self.checklist_states[index] = not self.checklist_states[index]
    def reset_fields(self, message:bool=True):
        """Resets all fields and checklist items"""
        confirmation = True
        if message:
            confirmation = messagebox.askyesno("Reset Confirmation", "Are you sure you want to reset all fields and checklist?")
        if confirmation:
            for entry in self.notes_section + self.fields_entry:
                entry.delete(0, tk.END)
            self.checklist_states = [False] * len(self.sections)
            for num, each in enumerate(self.checkboxes):
                each.checkbox_var.set(self.checklist_states[num])
    def create_button(self, button_text:str, button_command, button_column:int):
        """Creates a button with the given text, command, and column"""
        button = tk.Button(self.master, text=button_text, command=button_command)
        rows,columns = self.master.grid_size()
        button.grid(row=len(self.sections) + rows, column=button_column, columnspan=1, pady=10, sticky="")
        return button
    def create_buttons(self):
        """Creates Reset, Save, and Load buttons"""
        self.reset_button = self.create_button("Reset", self.reset_fields, 0)
        self.save_button = self.create_button("Save", self.save_state, 1)
        self.load_button = self.create_button("Load", self.load_state, 2)
    def save_state(self):
        """Saves the current state of the checklist"""
        state = {
            'checklist type': self.checklist_title,
            'fields': [field.get() for field in self.fields_entry],
            'checklist_states': self.checklist_states,
            'notes': [entry.get() for entry in self.notes_section]
        }
        with open('checklist_state.txt', 'w') as f: #maybe use self.CHECKLIST_STATE_FILE
            for key, value in state.items():
                f.write(f"{key}: {value}\n")
    def load_state(self):
        """Loads the saved state of the checklist"""
        try:
            with open('checklist_state.txt', 'r') as f:
                state = {}
                for line in f:
                    key, value = line.strip().split(': ')
                    if key == 'checklist type':
                        state[key] = value
                    elif key in ['fields', 'notes']:
                        state[key] = [elem.strip("[]'") for elem in value.split(", ")]
                    elif key == 'checklist_states':
                        str_to_bool = lambda x: True if x == "True" else False
                        save_states = [str_to_bool(v.strip("[]")) for v in value.split(', ')]
                        state[key] = save_states
                self.reset_fields(False)
                self.checklist_title = state["checklist type"]
                self.permit_entry.insert(0, state["fields"][0])
                self.address_entry.insert(0, state["fields"][1])
                self.parcel_entry.insert(0, state["fields"][2])
                self.checklist_states = [box for box in state["checklist_states"]]
                for num, each in enumerate(self.checkboxes):
                    each.checkbox_var.set(self.checklist_states[num])
                for num, entry in enumerate(self.notes_section):
                    entry.insert(0, state["notes"][num])
        except FileNotFoundError:
            self.checklist_states = [False] * len(self.sections)
        
        # see if you like this code
        # try:
        #     with open(self.CHECKLIST_STATE_FILE, 'r') as f:
        #         state = self._parse_state_file(f)
        #         self.reset_fields(False)
        #         self._populate_state(state)
        # except FileNotFoundError:
        #     self.checklist_states = [False] * len(self.sections)
        # except ValueError as e:
        #     print(f"Error loading state: {e}")

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
                    "Deem Complete",
                    "Move to Distribution"
                    ]
BR_PLM_CHECKLIST:list = ["Check Jurisdiction",
                    "Check for duplicate permits",
                    "Check for Violations",
                    "Check Licensed Professionals Attached",
                    "Check if Private Provider",
                    "Check for open permits",
                    "Check submitted documents",
                    "Check NOC requirement",
                    'Enter or verify "Standard Description" and use established naming convention',
                    "Deem Complete",
                    "Tell Krystal she did a good job"
                    ]
BLAME_ROBERT:list = [
    "Organize Desk",
    "hello",
    "hahaha",
    "well I dont know what to put here"
                     ]
checklist = BR_RMR_CHECKLIST

def add_tab(notebook,tab_text):
    new_frame = ttk.Frame(notebook)
    notebook.add(new_frame,text=tab_text)
    return new_frame

def tab_changed(event):
    selected_tab = event.widget.tab(event.widget.select(), "text")
    print(f"Selected tab: {selected_tab}")

def click_add_new_tab(event):
    selected_tab = event.widget.tab(event.widget.select(), "text")
    if selected_tab == "+":
        new_tab = add_tab(notebook,"New Tab")
        notebook.insert("end",add_tab_function)
        notebook.select(new_tab)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pinellas County Permit Utility")
    
    notebook = ttk.Notebook(root)
    notebook.pack()
    # tab_list = notebook.winfo_children() #gets a list of child widgets

    tab1 = add_tab(notebook,title)
    content_of_tab1 = ChecklistGUI(tab1,checklist,title)
    # tab1 = tk.Frame(notebook)
    # notebook.add(tab1, text=title)
    
    tab2 = add_tab(notebook,"Robert")
    content_of_tab2 = ChecklistGUI(tab2,BLAME_ROBERT,"BR-PLB Checklist")
    # tab2 = tk.Frame(notebook)
    # notebook.add(tab2, text="Tab 2")



    #leave last
    add_tab_function = add_tab(notebook,tab_text="+")
    notebook.bind("<<NotebookTabChanged>>", click_add_new_tab)


    def on_closing():
        content_of_tab1.save_state()
        root.destroy()
    #to close the window
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()