import customtkinter as ctk
import CTkListbox as ctl



app = ctk.CTk()
app.geometry("800x600")
app.title("TaskManager")
app.resizable(False, False)
app.grid_propagate(False)

check = ctk.StringVar(value="not_completed")

def completed_check():
    check.get()

list_frame = ctk.CTkFrame(app, width=230, height=560)
list_frame.grid(row=0, column=0, padx=5, pady=5)

list_information_frame = ctk.CTkFrame(app, width=500, height=560)
list_information_frame.grid(row=0, column=1, padx=5, pady=5, sticky="n")
list_information_frame.grid_columnconfigure(0, weight=0)
list_information_frame.grid_rowconfigure(0, weight=0)

listbox = ctl.CTkListbox(list_frame, width=230, height=560, command=None)
listbox.grid(row=0, column=0, padx=5, pady=5)

listitem_title = ctk.CTkLabel(list_information_frame, textvariable=None)
listitem_title.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

textbox = ctk.CTkTextbox(
    list_information_frame,
    width=490,
    height=300,
)
textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nwes")

tasktitle_text = ctk.CTkLabel(list_information_frame, text="Your task title:")
tasktitle_text.grid(row=2, column=0, padx=5, pady=5, sticky="w")

tasktitle_entry = ctk.CTkEntry(list_information_frame)
tasktitle_entry.grid(row=3, column=0, padx=5, pady=5, sticky="w")

task_completed = ctk.CTkCheckBox(
    list_information_frame, 
    text="Completed", 
    command=completed_check, 
    variable=check, 
    onvalue="completed", 
    offvalue="not_completed"
)
task_completed.grid(row=4, sticky="w")

app.mainloop()