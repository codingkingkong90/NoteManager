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

notetitle_entry = ctk.CTkEntry(list_information_frame, placeholder_text="Enter a title for your note", width=170)
notetitle_entry.grid(row=3, column=0, padx=5, pady=5, sticky="w")

notetitle_save = ctk.CTkButton(list_information_frame, text="Save Title")
notetitle_save.grid(row=4, column=0, padx=5, pady=5, sticky="w")

notesave = ctk.CTkButton(list_information_frame, text="Save Note")
notesave.grid(row=5, column=0, padx=5, pady=5, sticky="w")

app.mainloop()